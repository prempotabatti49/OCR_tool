from fastapi import APIRouter,  UploadFile, File
# from app.ingestion.ingestion_utils import ingest_document
# from app.services.aws_services import upload_file_to_s3
from app.services.ingestion_service import pdf_to_images, image_to_base64, run_ocr
import os
import json

router = APIRouter(prefix="/upload_doc", tags=["ingest"])
print("Current working directory:", os.getcwd())

@router.post("/")
async def upload_pdf_document(file: UploadFile = File(...)):
    ## Steps
    # Upload the document in S3 bucket
    # upload_file_to_s3(file.file, "your-bucket-name", file.filename)
    # Convert pdf to images
    images = await pdf_to_images(file)
    # save the images in a temp folder
    file_name = file.filename.split(".")[0]
    for i, image in enumerate(images):
        save_path = os.path.join(os.getcwd(), "app", "temp_images")
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        image.save(os.path.join(save_path, f"page_{i+1}.png"), "png")

    extracted_pages = []
    # For each page, take a screenshot
    for page_number, image in enumerate(images):
        # Convert image → base64
        base64_image = image_to_base64(image)
        # Send to OCR model
        structured_text = await run_ocr(base64_image)
        extracted_pages.append(
            {
                "page": page_number + 1,
                "content": structured_text
            }
        )
    # Save the extracted text in a json file
    save_file_path = os.path.join(os.getcwd(), "app", "extracted_data")
    if not os.path.exists(save_file_path):
        os.makedirs(save_file_path)
    file_path = os.path.join(save_file_path, f"{file_name}_extracted.json")
    with open(file_path, "w") as f:
        json.dump(extracted_pages, f, indent=4)
    return {"message": "Document uploaded and processed successfully"}


