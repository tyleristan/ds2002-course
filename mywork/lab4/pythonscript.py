#!/usr/bin/env python3

import boto3
import urllib
import os

url = "https://upload.wikimedia.org/wikipedia/commons/9/9e/Davidraju_IMG_3465.jpg"
save_path = "~/Downloads/image.jpg"
urllib.request.urlretrieve(url,'image.jpg')

s3 = boto3.client('s3', region_name='us-east-1')

bucket_name = 'ds2002-twg2nk'
object_name = "image.jpg"
expires_in = 604800

resp = s3.put_object(
    Body = object_name,
    Bucket = bucket_name,
    Key = object_name
)

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
)
print(response)

presigned url: https://ds2002-twg2nk.s3.amazonaws.com/image.jpg?AWSAccessKeyId=ASIA6GBMHAX5LI7S3HE2&Signature=GbNZMg4QrE8Efo3RHjUTXHQom%2Bk%3D&x-amz-security-token=FwoGZXIvYXdzEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDKe3Ao0MK8yQ6scSUiLEAUhnRuTlBKy97iWgo8dfB%2Bh3r%2FucaHzc1WRiqy2pnq52BkYH7AMg%2Fw%2FjAihhQ3bmkZXFinZMVh0sokT%2FtOlEAIyhcYWJHVkbjek28stLnze3c129lWCNDYIgXCuLObm0wAtJ4LLz5HRwoaY2BzobrOS%2BikBJ075r44yBwk20366pNTPLukLbAn%2BEmcAn8y17LJCnJEp8x7%2Fmx90GyFdy0EJ%2FDiGW75EsA4pK6xb1U14mFpBWgl2xG4wTqjrsMm1KJsJoEWko4MbSrwYyLWMXIoKIFzIDXdSJTFoMGM%2BZDI%2B9Ik6ZKd8yQGjZHuk9l7Wj8GrHS2BD4aP%2BYg%3D%3D&Expires=1711144934
