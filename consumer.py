#!/usr/bin/env python

import wm_parser							# modulo locale

import pika								# import e connessione RMQ
credentials = pika.PlainCredentials('root', 'washomatic')
parameters = pika.ConnectionParameters('52.210.163.71',
                                       5672,
                                       '/',
                                       credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

def callback(ch, method, properties, msg):				# running task
	print(" [x] Received %r" % msg)
	wm_parser.parse(msg)						# parsing di cio' che arriva
	out_file = open("log.txt","a")					# log di ciò che arriva
	out_file.write(msg)
	out_file.close()


channel.basic_consume(callback, queue='coda', no_ack=True)		# connessione a una coda

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()						# sta in ascolto della coda
