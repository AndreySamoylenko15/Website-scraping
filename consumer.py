import json
import os
import sys
import time
from models import Contact
import pika


credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()


queue_name = "email_queue"
channel.queue_declare(queue=queue_name)

def process_message(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message["contact_id"]
    contact = Contact.objects.get(id=contact_id)

    print(f"Sending email to {contact.email}...")

    contact.notified = True
    contact.save()

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=queue_name, on_message_callback=process_message)

print("Consumer is waiting for message. To exit, press Ctrl+C")
channel.start_consuming()