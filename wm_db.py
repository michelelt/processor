import mysql.connector

_user		= "root"
_password	= "washomatic"
_host		= "52.210.163.71"
_database	= "washomatic"

def insert_weight(box_id, weight):
	cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
	cursor = cnx.cursor()
	# Devo prima salvare la lettura precedente nell'altro campo della tabella
	query = """UPDATE box SET box_current_weight = %s WHERE box_id = %s"""
	cursor.execute(query, (weight, box_id))						# Inserimento dei miei parametri
	cnx.commit()
	cursor.close()
	cnx.close()
