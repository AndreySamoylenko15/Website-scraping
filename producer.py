import json
from datetime import datetime
from models import Contact
import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

queue_name = "email_queue"
channel.queue_declare(queue=queue_name)

fake_contacts = [
    {"full_name": "John Doe", "email": "john@example.com"},
    {"full_name": "Jane Smith", "email": "jane@example.com"},
    ]

for contact in fake_contacts:
    contact_obj = Contact(full_name=contact["full_name"], email=contact["email"])    
    contact_obj.save()

    massage = {"contact_id": str(contact_obj.id)}
    channel.basic_publish(exchange="", routing_key=queue_name, body=json.dumps(massage))

print("Contacts saved and massage published to RabbitMQ")

connection.close()