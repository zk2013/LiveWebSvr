import mysql.connector
from mysql.connector import errorcode

if __name__ == '__main__':
	print('--------------------')
	print('\r\nstart test python sql\r\n')
	try:
		cnx = mysql.connector.connect(user='zk2013', password='fucklq',host='127.0.0.1',database='livedb')
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		print('connect ok')
		cnx.close()
	print('--------------------\r\n')

class LiveDbProxy:
	# db connection
	def __init__(self,dbuser,dbpasswd,dbhost='127.0.0.1', database='livedb'):
		self._dbuser = dbuser
		self._dbpasswd = dbpasswd
		self._dbhost = dbhost
		self._database = database

	def openDb(self):
		try:
			self.cnx = mysql.connector.connect(user=self._dbuser, password=self._dbpasswd,host=self._dbhost,database=self._database)
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Something is wrong with your user name or password")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Database does not exist")
			else:
				print(err)
			return False
		else:
			return True
	
	def closedb(self):
		self.cnx.close()
	
	# logic
	def login(self,account,password):
		print('query db for login')
		ret = False
		msg = None
		cursor = self.cnx.cursor()
		query = 'select * from user_info where phone=%s and passwd=%s;'
		cursor.execute(query,(account,password))
		result_set = cursor.fetchall()
		print(result_set)
		if result_set:
			ret = True
			for row in result_set:
				msg = {"uid":row[0],"nickname":row[4],"last_login_time":row[32]}
			
		cursor.close()
		return [ret,msg]

class LiveDbProxyholder:
	dbproxy = None

	@staticmethod
	def set_dbproxy(db):
		LiveDbProxyholder.dbproxy = db
	
	@staticmethod
	def get_dbproxy():
		return LiveDbProxyholder.dbproxy