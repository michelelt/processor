#!/usr/bin/env python
import json

CMDs = {'WEIGHT_CHANGED':'0'}						# dictionary con la lista dei comandi

def parse(msg):
	try:								# per json non corretti si solleva un'eccezione
		arr = json.loads(msg)
	except ValueError:
		print "Invalid Json"

	print "Valid Json"

	if arr['CMD'] == CMDs['WEIGHT_CHANGED']:			# "switch" sui diversi comandi che arrivano
		print "Received command: WEIGHT_CHANGED"
		#Qui check sui dati e scrittura su DB
	else:
		print "Comando non riconosciuto"

