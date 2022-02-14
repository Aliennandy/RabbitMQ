#!/usr/bin/env python
import pika
import ssl
credentials = pika.PlainCredentials('guest', 'guest')
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
parameters = pika.ConnectionParameters(host='ec2-13-126-58-1.ap-south-1.compute.amazonaws.com',
                                       port=5671,
                                       virtual_host='/',
                                       credentials=credentials,
                                       ssl_options=pika.SSLOptions(context)
                                       )

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()