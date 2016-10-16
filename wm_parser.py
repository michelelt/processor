#!/usr/bin/env python
import json
import wm_db
CMDs = {'WEIGHT_CHANGED':'0'}						# dictionary con la lista dei comandi

def validController(msg):
	try:
		controller_id = msg['controller_id']
	except KeyError:
		print "invalid key"
		return -1	
	if not controller_id.isnumeric():		
		print "non numeric controller id"
		return False
	if not wm_db.controllerExists(controller_id):
		print "this controller does not exist"
		return False
	return True


def validBox(msg):
	try:
		box_id = msg['box_id']
	except KeyError:
		print "invalid key"
		return -1	
	if not box_id.isnumeric():
		print "non numeric box id"
		return False
	if not wm_db.boxExists(box_id):
		print "this box does not exist"
		return False
	return True


def validWeight(msg):
	try:
		weight = msg['w']
	except KeyError:
		print "invalid key"
		return False	
	if not weight.isnumeric():
		print "non numeric value for weight"
		return False
	weight = float(weight)
	if weight < 0:
		print "invalid weight"
		return False
	return True

def parse(msg):
	try:
		arr = json.loads(msg)
	except ValueError:
		print "Invalid Json"

	print "Valid Json"
	
	try:
		cmd = arr['CMD']
	except KeyError:
		print "invalid key"
		return -1

	if cmd == CMDs['WEIGHT_CHANGED']:
		if not validController(arr) or not validBox(arr) or not validWeight(arr):
			return -1
		print "Received command: WEIGHT_CHANGED - new weight: "+ arr['w'] +"kg for box "+ arr['box_id']
		wm_db.insert_weight(arr['box_id'], arr['w'])
	else:
		print "Command not found"


