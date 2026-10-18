import boto3
from PIL import Image
from io import BytesIO
from urllib.parse import unquote_plus
import os

s3 = boto3.client("s3")
DEST_BUCKET = "giridhar-image-resize-2026-890"

def lambda_handler(event, context):
    record = event["Records"][0]
    source_bucket = record["s3"]["bucket"]["name"]
    key = unquote_plus(record["s3"]["object"]["key"])

    response = s3.get_object(Bucket=source_bucket, Key=key)
    image = Image.open(BytesIO(response["Body"].read()))
    image.thumbnail((300, 300))

    output = BytesIO()
    fmt = image.format or "JPEG"

    if fmt.upper() == "JPG":
        fmt = "JPEG"
    if fmt.upper() not in ("JPEG", "PNG", "WEBP"):
        fmt = "JPEG"
    if fmt == "JPEG" and image.mode not in ("RGB", "L"):
        image = image.convert("RGB")

    image.save(output, format=fmt)
    output.seek(0)

    output_key = "resized-" + os.path.basename(key)
    s3.put_object(
        Bucket=DEST_BUCKET,
        Key=output_key,
        Body=output.getvalue(),
        ContentType=response.get("ContentType", "image/jpeg")
    )

    return {
        "statusCode": 200,
        "body": f"Resized image saved as {output_key}"
    }