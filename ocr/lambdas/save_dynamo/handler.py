import boto3

ddb = boto3.resource("dynamodb", endpoint_url="http://localhost:4566")
table = ddb.Table("InvoiceResult")


def handler(event, context):
    for r in event["records"]:
        table.put_item(
            Item={"caseId": event["caseId"], "invoiceNo": r["invoiceNo"], **r}
        )
    return {"status": "OK"}
