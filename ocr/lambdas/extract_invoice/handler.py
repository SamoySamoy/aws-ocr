from pydantic import BaseModel, ValidationError
from typing import List
from prompt import build_prompt
from llm_client import MockBedrockClient

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

llm = MockBedrockClient()

def handler(event, context):
    prompt = build_prompt(event["documentText"])
    response = llm.extract(prompt)

    try:
        validated = Output(
            caseId=event["caseId"],
            records=response["records"]
        )
    except ValidationError:
        raise Exception("UnprocessableDocument")

    return validated.model_dump()
