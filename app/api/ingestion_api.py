from fastapi import APIRouter,  UploadFile, File
from app.ingestion.ingestion_utils import ingest_document
from app.services.aws_services import upload_file_to_s3
from app.services.ingestion_service import pdf_to_images, image_to_base64, run_ocr
import os

router = APIRouter(prefix="/upload_doc", tags=["ingest"])
print("Current working directory:", os.getcwd())

@router.post("/")
async def upload_pdf_document(file: UploadFile = File(...)):
    ## Steps
    # Upload the document in S3 bucket
    # upload_file_to_s3(file.file, "your-bucket-name", file.filename)
    # Convert pdf to images
    images = pdf_to_images(file)
    # save the images in a temp folder
    file_name = file.filename.split(".")[0]
    for i, image in enumerate(images):
        save_path = os.path.join(os.getcwd(), "app", "temp_images")
        if "temp_images" not in os.listdir():
            os.makedirs("temp_images")

        image.save(f"temp/page_{i}.png", "PNG")

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

    # Convert the image in base64 form
    # Send the base64 image to the OCR model and get the text in structured format
    # Store the structured data in the database
    return ingest_document()


