class PROMPTS:
    def __init__(self):
        pass

    def ocr_prompt(self):
        prompt = f"""
You are an expert document understanding system specialized in reading handwritten receipt books.
The reciept can be in any language and the handwriting can be of any quality.
The language can be either English, or Hindi, or Marathi, or Telugu, or any other language, or a mix of them.

You will receive an image (base64 encoded) of a page from a receipt book.

These receipt books are often handwritten and may vary in structure between different books. However, within a single page the receipts typically follow a repetitive structure.

Your task is to carefully analyze the page and extract all information from every receipt present on the page.

Important instructions:

1. The receipts may contain both printed structure and handwritten content.
2. The layout may vary slightly between pages or books.
3. There may be handwritten notes, corrections, or comments written in margins or sides of the page.
4. Some fields may be missing or unclear due to handwriting quality.
5. Multiple receipts may exist on the same page.

Extraction rules:

• Identify each individual receipt separately.
• Extract all visible fields from each receipt.
• If a field label exists, use that as the key name.
• If the field label is unclear, infer a meaningful key name.
• Preserve the exact text as written (do not normalize unless obvious).
• Capture handwritten margin notes or side comments separately.
• If a value is unclear, mark it as uncertain.
• Do not hallucinate values.

Extract all the fields and values you can find on the receipt. 

The receipt format may vary, so you must also capture any additional fields that appear on the receipt.

If multiple receipts exist, return them as separate objects.

Return ONLY valid JSON.

Output format:

{{
  "page_summary": {{
    "total_receipts_detected": number,
    "general_page_notes": []
  }},
  "receipts": [
    {{
      "receipt_number": "",
      "date": "",
      "payer_name": "",
      "amount": "",
      "payment_method": "",
      "purpose": "",
      "fields_detected": {{
        "field_name_1": "value",
        "field_name_2": "value"
      }},
      "handwritten_notes": [],
      "margin_comments": [],
      "uncertain_fields": []
    }}
  ]
}}

Additional instructions:

• Include every visible field from the receipt even if it does not match the common ones listed above.
• Preserve original text exactly as written.
• Do not remove currency symbols.
• If handwriting is difficult to read, include the best possible interpretation and mark it uncertain.
• If the page contains crossed-out entries or corrections, include them under handwritten_notes.

First carefully analyze the layout of the page and identify the boundaries of each receipt.
Then extract fields for each receipt individually.

Accuracy is more important than guessing.

Return only the JSON output.
"""
        return prompt