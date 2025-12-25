import json
from pydantic import BaseModel, ValidationError
from typing import List

class Record(BaseModel):
    receivedDate: str
    clinicName: str
    visitDate: str
    invoiceNo: str
    particular: str
    currency: str
    amount: float

class Output(BaseModel):
    caseId: str
    records: List[Record]

def mock_bedrock_llm(text: str):
    # MOCK for LocalStack – explain this in interview
    if "ASIA" in text:
        return [{
            "receivedDate": "2025-01-12T00:00:00Z",
            "clinicName": "ASIA Dental",
            "visitDate": "2025-01-10T00:00:00Z",
            "invoiceNo": "ASIA-001",
            "particular": "Nguyen Van A",
            "currency": "VND",
            "amount": 1500000
        }]
    else:
        return [
            {
              "receivedDate": "2025-01-11T00:00:00Z",
              "clinicName": "JGH Hospital",
              "visitDate": "2025-01-08T00:00:00Z",
              "invoiceNo": f"JGH-00{i}",
              "particular": "Patient X",
              "currency": "VND",
              "amount": 1000000
            } for i in range(1,5)
        ]

def handler(event, context):
    records = mock_bedrock_llm(event["documentText"])

    try:
        validated = Output(
            caseId=event["caseId"],
            records=records
        )
    except ValidationError:
        raise Exception("UnprocessableDocument")

    return validated.dict()
