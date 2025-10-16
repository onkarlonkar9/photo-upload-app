import json
import boto3
import base64
import uuid

s3 = boto3.client('s3')
BUCKET = "my-photo-upload-bucket-v1"

def lambda_handler(event, context):
    try:
        print("Incoming event:", event)

        body = event.get("body")
        if body is None:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing body"})}

        body = json.loads(body)
        if "image" not in body:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing 'image' field in body"})}

        image_data = base64.b64decode(body["image"])
        file_name = f"{uuid.uuid4()}.jpg"
        s3.put_object(Bucket=BUCKET, Key=file_name, Body=image_data, ContentType="image/jpeg")

        image_url = f"https://{BUCKET}.s3.amazonaws.com/{file_name}"

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "Image uploaded successfully!",
                "url": image_url
            })
        }

    except Exception as e:
        print("Error:", str(e))
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
