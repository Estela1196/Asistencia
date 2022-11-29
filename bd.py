import pymysql

class DataBase:
	def __init__(self):
		self.connection = pymysql.connect(
			host ='localhost',
			user='root',
			password='',
			db='asistencia'
		)
		self.cursor= self.connection.cursor()
		print ("Conexion exitososa a la base de datos")


	def select(self):
		sql = 'select * from alumnos'
		
		try:
			self.cursor.execute(sql)
			usuario= self.cursor.fetchone()
			
			print("ID: ", usuario[0])
			print("Nombre: ", usuario[1])
			print("ApellidoA : ", usuario[2])
			print("ApellidoM : ", usuario[3])
			print("Carrera : ", usuario[4])
		except Exception as e:
			raise
