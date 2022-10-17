# This py file publish message in port and the other py files catch this message.
import pika
import json
import uuid


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


order = {
    'id': str(uuid.uuid4()),
    'user_email': 'your_mail@example.com',
    'product': 'Computer',
    'quantity': 1
}

channel.basic_publish(
    exchange='order',
    routing_key='order.notify',
    body=json.dumps({'user_email': order['user_email']})
)

print(' [x] Sent notify message')

channel.basic_publish(
    exchange='order',
    routing_key='order.report',
    body=json.dumps(order)
)

print(' [x] Sent report message')

connection.close()
