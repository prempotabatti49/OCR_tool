from app.utils.utils import stitch_base64_messages
import fitz
import base64
from app.prompt_repo.ocr_prompt import PROMPTS
from app.utils.openai_llm_call import call_llm_openai
import json

async def pdf_to_images(file):
    contents = await file.read()
    doc = fitz.open(stream=contents, filetype="pdf")
    images = []
    for page in doc:
        pix = page.get_pixmap(dpi=200)
        images.append(pix)
    doc.close()
    return images


def image_to_base64(image):
    return base64.b64encode(image.tobytes("png")).decode("utf-8")


async def run_ocr(base64_image):
    prompt = PROMPTS().ocr_prompt()
    # create message to pass to LLM, including base64 image and the prompt
    message = stitch_base64_messages(prompt, base64_image)
    output = await call_llm_openai(message)
    # Parse the output into json format
    output = json.loads(output.strip().replace("```json", "").replace("```", ""))

    return output

