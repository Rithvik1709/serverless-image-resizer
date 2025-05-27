import boto3
from PIL import Image
import io
import os

s3 = boto3.client('s3')

def resize_image(image_data):
    image = Image.open(io.BytesIO(image_data))
    image = image.resize((128, 128))  # Resize to 128x128
    buffer = io.BytesIO()
    image.save(buffer, format='JPEG')
    buffer.seek(0)
    return buffer
 
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    image_obj = s3.get_object(Bucket=bucket, Key=key)
    image_data = image_obj['Body'].read()

    resized_image = resize_image(image_data)

    resized_key = f"resized/{key}"
    s3.put_object(Bucket=bucket, Key=resized_key, Body=resized_image, ContentType='image/jpeg')

    return {
        'statusCode': 200,
        'body': f'Image resized and saved as {resized_key}'
    }
