AWS Lambda Image Resizing

Project Overview

This project automatically resizes images uploaded to an Amazon S3 input bucket using AWS Lambda, Python, and the Pillow library. The resized images are stored in a separate S3 output bucket.

AWS Services Used

- Amazon S3: Stores original and resized images.
- AWS Lambda: Runs the image resizing function.
- Python: Implements the processing logic.
- Pillow (PIL): Resizes images.

Workflow

1. Upload an image to the input S3 bucket.
2. The S3 event triggers the Lambda function.
3. Lambda reads the image from the input bucket.
4. Pillow resizes the image to fit within 300 × 300 pixels while maintaining its aspect ratio.
5. The resized image is saved in the output S3 bucket with the "resized-" prefix.

Configuration

- Input bucket: "giridhar-lambda-input-2026-8317"
- Output bucket: "giridhar-image-resize-2026-890"
- Lambda function: "ImageResizeFunction"
- Output filename format: "resized-originalfilename.png"

Expected Result

When an image is uploaded to the input bucket, a resized copy should appear in the output bucket.

Notes

The Lambda function requires the Pillow dependency and appropriate S3 read/write permissions. Keep the input and output buckets separate to avoid recursive triggers.

Author

Giridhar
Jeevan
