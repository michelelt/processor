import mysql.connector

_user		= "root"
_password	= "washomatic"
_host	= "52.209.57.241"
_database	= "washomatic"


def insert_weight(box_id, weight):
	current_weight = get_current_weight(box_id)							# l'ultimo current_weight
	set_box_last_weight(box_id, current_weight)							# viene spostato su last_weight nel db
	cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
	cursor = cnx.cursor()
	query = """UPDATE box SET box_current_weight = %s WHERE box_id = %s"""
	cursor.execute(query, (weight, box_id))
	cnx.commit()
	cursor.close()
	cnx.close()


# restituisce l'ultimo peso registrato relativamente a un box dato
def get_current_weight(box_id):
	cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
	cursor = cnx.cursor(buffered=True)
	query = """SELECT box_current_weight FROM box WHERE box_id = %s"""
	cursor.execute(query, (box_id,))
	cnx.commit()
	for (box_current_weight,) in cursor:
		cursor.close()
		cnx.close()
		return box_current_weight


# Imposta un valore per la vecchia lettura del peso
def set_box_last_weight(box_id, weight):
	cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
	cursor = cnx.cursor()
	query = """UPDATE box SET box_last_weight = %s WHERE box_id = %s"""
	cursor.execute(query, (weight, box_id))
	cnx.commit()
	cursor.close()
	cnx.close()


# Restituisce un booleano sulla presenza o meno del box nel db
def boxExists(box_id):
	cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
	cursor = cnx.cursor(buffered=True)
	query = """SELECT * FROM box WHERE box_id = %s"""
	cursor.execute(query, (box_id,))
	cnx.commit()
	result = True
	if cursor.rowcount == 0:
		result = False
	cursor.close()
	cnx.close()
	return result


# Restituisce un booleano sulla presenza o meno del controller nel db
def controllerExists(controller_id):
	cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
	cursor = cnx.cursor(buffered=True)
	query = """SELECT * FROM controller WHERE controller_id = %s"""
	cursor.execute(query, (controller_id,))
	cnx.commit()
	result = True
	if cursor.rowcount == 0:
		result = False
	cursor.close()
	cnx.close()
	return result
 
 #restituisce un booleano sulla presenza del tipo del capo
def item_typeExist(item_type_id):
    cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
    cursor = cnx.cursor(buffered=True)
    query = """SELECT * FROM item_type WHERE item_type_id = %s"""
    cursor.execute(query, (item_type_id,))
    cnx.commit()
    result = True
    if cursor.rowcount == 0:
        result = False
    cursor.close()
    cnx.close()
    return result

 #restituisce un booleano sulla presenza del materiale del capo
def item_materialExist(item_material_id):
    cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
    cursor = cnx.cursor(buffered=True)
    query = """SELECT * FROM item_material WHERE item_material_id = %s"""
    cursor.execute(query, (item_material_id,))
    cnx.commit()
    result = True
    if cursor.rowcount == 0:
        result = False
    cursor.close()
    cnx.close()
    return result
    
#restituisce un booleano sulla presenza del colore del capo
def item_colorExist(item_color_id):
    cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
    cursor = cnx.cursor(buffered=True)
    query = """SELECT * FROM item_color WHERE item_color_id = %s"""
    cursor.execute(query, (item_color_id,))
    cnx.commit()
    result = True
    if cursor.rowcount == 0:
        result = False
    cursor.close()
    cnx.close()
    return result

def userExist(user_id):
    cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
    cursor = cnx.cursor(buffered=True)
    query = """SELECT * FROM user WHERE user_id = %s"""
    cursor.execute(query, (user_id,))
    cnx.commit()
    result = True
    if cursor.rowcount == 0:
        result = False
    cursor.close()
    cnx.close()
    return result


def insert_new_item(user_id, item_name, item_type_id, item_material_id, item_color_id):
    cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
    cnx.start_transaction(readonly=False)
    
    cursor = cnx.cursor()
    
    query = """INSERT INTO item (item_name, item_type, item_material, item_color) """\
            """VALUES (%s, %s, %s, %s) """
    cursor.execute(query, (item_name, int(item_type_id), int(item_material_id), int(item_color_id)))
    item_id = str(cursor.lastrowid)
    #print item_id
    
    query = """INSERT INTO user_has_item (user_id, item_id) """\
            """VALUES (%s, %s)"""
    cursor.execute(query, (int(user_id), int(item_id)))

    cnx.commit()
    
    cursor.close()
    cnx.close()
    

