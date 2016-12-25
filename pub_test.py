#!/usr/bin/env python
import pika
credentials = pika.PlainCredentials('root', 'washomatic')			# Connessione con RMQ
parameters = pika.ConnectionParameters('52.209.57.241',
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='coda', durable=True)

with open("msg") as f:								# Leggiamo il messaggio da un file che viene piu' comodo
	msg = f.readlines()

channel.basic_publish(exchange='', routing_key='coda', body=msg[0].strip())	# Invio a RMQ
print(" [x] Sent "+ msg[0])
connection.close()
