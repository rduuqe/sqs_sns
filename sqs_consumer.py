import os

import boto3
import json
import time
import dotenv

dotenv.load_dotenv()

sqs_client = boto3.client('sqs',
                          aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                          aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
                          region_name='us-east-2')
queue_url = os.environ['QUEUE_URL']


def process_message(message):
    message_body = json.loads(message['Body'])

    message_id = message_body['MessageId']
    message_content = message_body['Message']
    print(f"Procesando mensaje con ID: {message_id}")
    print(f"Contenido del mensaje: {message_content}")

    # ...

    if 'ReceiptHandle' in message:
        receipt_handle = message['ReceiptHandle']
        # Delete the message using the receipt handle
        sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
    else:
        print("Mensaje no contiene ReceiptHandle key!")


while True:
    messages = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        VisibilityTimeout=20
    )
    if 'Messages' in messages:

        for message in messages['Messages']:
            process_message(message)
    else:
        time.sleep(5)
