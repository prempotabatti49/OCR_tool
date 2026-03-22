def stich_message(prompt, base64_image):
    return [
        {"role": "user", 
         "content": [
            {"type": "text", "text": prompt},
            {"type": "image", "data": base64_image}
            ]
        }
    ]