#This py file catching message from publish and reporting the message details.

import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


queue = channel.queue_declare('order_report')
queue_name = queue.method.queue

channel.exchange_declare(
    exchange='order',
    exchange_type='direct'
)

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.report'  # binding key
)


def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(' [x] Generating report')
    print(f"""
    ID: {payload.get('id')}
    User Email: {payload.get('user_email')}
    Product: {payload.get('product')}
    Quantity: {payload.get('quantity')}
    """)

    print(' [x] Done')
    print(' [x] Waiting for report messages.')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue_name, callback)

print(' [x] Waiting for report messages.')

channel.start_consuming()