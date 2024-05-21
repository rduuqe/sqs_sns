import os
import sys

import boto3
import dotenv

dotenv.load_dotenv()

sns_client = boto3.client('sns',
                          aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                          aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                          region_name='us-east-2')

response = sns_client.publish(
    TopicArn=os.environ['TOPIC_ARN'],
    Message=sys.argv[1],
    Subject='Publicación de TOPIC'
)

print(f"Message published: {response['MessageId']}")