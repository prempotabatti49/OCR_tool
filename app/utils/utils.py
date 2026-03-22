def stitch_base64_messages(prompt, base64_image):
    return [
        {"role": "user", 
         "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
            ]
        }
    ]