#This py file catching message from publish, and notifying us.

import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


queue = channel.queue_declare('order_notify')
queue_name = queue.method.queue

channel.exchange_declare(
    exchange='order',
    exchange_type='direct'
)

channel.queue_bind(
    exchange='order',
    queue=queue_name,
    routing_key='order.notify'  # binding key
)


def callback(ch, method, properties, body):
    payload = json.loads(body)
    print(' [x] Notifying {}'.format(payload['user_email']))
    print(' [x] Done')
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(queue_name,callback )

print(' [x] Waiting for notify messages.')

channel.start_consuming()