import json
    
def main(event, context):
    body = json.loads(event["Records"][0]["body"])

    bucket = body["Records"][0]["s3"]["bucket"]
    file = body["Records"][0]["s3"]["object"]
    bucket_name = bucket["name"]
    key = file["key"]
    size = file["size"]
    
    response = f"The file '{key}' has a size of {size}B and it's located in the bucket {bucket_name}"
    print(response)
    return {
        'statusCode' : 200,
        'body': json.dumps(response)
    }