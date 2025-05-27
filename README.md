# Serverless Image Resizer (AWS Lambda + S3)

Resize images automatically when uploaded to an S3 bucket, using AWS Lambda.

## Tech Stack

- AWS Lambda (Python)
- AWS S3
- AWS SAM CLI
- PIL (Pillow) for image processing


## Setup & Deploy

### 1. Install AWS SAM CLI
[Install Instructions](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/serverless-image-resizer.git
cd serverless-image-resizer
```
### 3. Install Dependencies
```bash
cd lambda
pip install -r requirements.txt -t .
```
### 4. Build and Deploy
```bash
sam build
sam deploy --guided
```
Enter a stack name (e.g., ImageResizerStack)
Choose AWS region
Confirm S3 bucket name for deployment artifacts
### 5. Upload Image to Trigger Resize
Open upload/index.html and:
Set the correct S3 bucket name
Upload an image
Check resized image under resized/ prefix in same bucket
