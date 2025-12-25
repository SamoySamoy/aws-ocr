ENDPOINT=http://localhost:4566

# S3
aws --endpoint-url=$ENDPOINT s3 mb s3://invoice-bucket

# DynamoDB
aws --endpoint-url=$ENDPOINT dynamodb create-table \
  --table-name InvoiceResult \
  --attribute-definitions \
    AttributeName=caseId,AttributeType=S \
    AttributeName=invoiceNo,AttributeType=S \
  --key-schema \
    AttributeName=caseId,KeyType=HASH \
    AttributeName=invoiceNo,KeyType=RANGE \
  --billing-mode PAY_PER_REQUEST

# push files 
aws --endpoint-url=http://localhost:4566 s3 cp \
  "data/jgh 4 cases.pdf" s3://invoice-bucket/jgh_4_cases.pdf

aws --endpoint-url=http://localhost:4566 s3 cp \
  "data/ASIA dental.pdf" s3://invoice-bucket/asia_dental.pdf