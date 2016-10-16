import mysql.connector

_user		= "root"
_password	= "washomatic"
_host		= "52.210.163.71"
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


# Restituisce un booleano sulla presenza o meno del box nel db
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

