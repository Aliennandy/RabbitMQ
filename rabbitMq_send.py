#!/usr/bin/env python
import pika
import sys

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

'''
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='tcp://13.233.174.205:1883'))

connection = pika.BlockingConnection(pika.ConnectionParameters('ec2-13-233-174-205.ap-south-1.compute.amazonaws.com',1883,'/',credentials))
    
'''   
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()