import boto3, uuid, io, pdfplumber

s3 = boto3.client("s3", endpoint_url="http://localhost:4566")

def handler(event, context):
    obj = s3.get_object(
        Bucket=event["bucket"],
        Key=event["key"]
    )

    pdf_bytes = obj["Body"].read()
    text = ""

    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    return {
        "caseId": str(uuid.uuid4()),
        "documentText": text
    }
