#!/usr/bin/env python3
import pika
credentials = pika.PlainCredentials('test', 'administrator')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='logs', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
