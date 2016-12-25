#!/usr/bin/env python
import json
import wm_db
CMDs = {'WEIGHT_CHANGED':'0', 'INSERT_NEW_ITEM':'1'}	# dictionary con la lista dei comandi

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
 
def validItemType(msg):
	try:
		item_type = unicode(msg['item_type'])
	except KeyError:
		print "invalid item type"
		return False
	if not item_type.isnumeric():
		print "non numeric value for item type"
		return False
	if not wm_db.item_typeExist(str(item_type)):
		print "invalid item type"
		return False
	return True
 
def validItemColor(msg):
	try:
		item_color = unicode(msg['item_color'])
	except KeyError:
		print "invalid item color"
		return False
	if not item_color.isnumeric():
		print "non numeric value for item color"
		return False
	if not wm_db.item_colorExist(str(item_color)):
		print "invalid item color"
		return False
	return True
 
def validItemMaterial(msg):
	try:
		item_material = unicode(msg['item_material'])
	except KeyError:
		print "invalid item material"
		return False
	if not item_material.isnumeric():
		print "non numeric value for item material"
		return False
	if not wm_db.item_materialExist(str(item_material)):
		print "invalid item material"
		return False
	return True
 
def validUser(msg):
	try:
		user = unicode(msg['user_id'])
	except KeyError:
		print "invalid user id"
		return False
	if not user.isnumeric():
		print "non numeric value for user id"
		return False
	if not wm_db.userExist(str(user)):
		print "invalid item user id"
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
          
    elif cmd == CMDs["INSERT_NEW_ITEM"]:
        if not validItemColor(arr) or not validItemMaterial(arr) or not validItemType or not validUser(arr):
            return -1
        print "Received command: INSER_NEW_ITEM. msg: " + msg
        wm_db.insert_new_item(arr["user_id"], arr["item_name"], arr["item_type"], arr["item_material"], arr["item_color"] )
    else:
        print "Command not found"


