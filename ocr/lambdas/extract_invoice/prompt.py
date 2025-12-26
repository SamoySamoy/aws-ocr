def build_prompt(document_text: str) -> str:
    return f"""
SYSTEM:
You are an insurance invoice extraction engine.
Return ONLY valid JSON.
Do not guess. Use null if missing.

USER:
Extract invoice records from the text below.

Schema:
{{
  "records": [
    {{
      "receivedDate": "YYYY-MM-DDThh:mm:ssZ",
      "clinicName": string,
      "visitDate": "YYYY-MM-DDThh:mm:ssZ",
      "invoiceNo": string,
      "particular": string,
      "currency": string,
      "amount": number
    }}
  ]
}}

Text:
\"\"\"
{document_text}
\"\"\"
"""
