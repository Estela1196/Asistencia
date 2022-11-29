from flask import Flask, render_template, request,redirect,url_for,flash
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'asistencia'
mysql=MySQL(app)

app.secret_key = 'secretkey'

@app.route('/')
def home(): 
	cur=mysql.connection.cursor()
	cur.execute('SELECT * FROM alumnos')
	data= cur.fetchall()	
	return render_template('home.html', contactos = data)
	

@app.route("/addAlumnos", methods=['POST'])
def addAlumnos():
	if request.method == 'POST':
		nombre=request.form['Nombre']
		apellidoP=request.form['ApellidoP']
		apellidoM=request.form['ApellidoM']
		carrera=request.form['Carrera']
		asistencia=request.form['Asistencia']
		cur=mysql.connection.cursor()
		cur.execute('INSERT INTO alumnos(Nombre,ApellidoP,ApellidoM,Carrera,Asistencia)Values(%s,%s,%s,%s,%s)',(nombre,apellidoP,apellidoM,carrera,asistencia))
		mysql.connection.commit()
		flash('Se agrego correctamente')
		return redirect(url_for('home'))

@app.route('/eliminar/<string:id>')
def eliminar(id):
	cur=mysql.connection.cursor()
	cur.execute('DELETE FROM alumnos WHERE Id_alumnos ={0}'.format(id))
	mysql.connection.commit()
	flash('Se elimino correctamente')	
	return redirect(url_for('home'))

@app.route('/addAsistencia/<id>')
def update(id):
	cur=mysql.connection.cursor()
	cur.execute('select * from alumnos WHERE Id_alumnos= %s',(id))
	data =cur.fetchone()
	data0=data[0]
	data5=data[5]
	cur.execute('UPDATE alumnos SET asistencia = %s WHERE Id_alumnos = %s',(data5+1,data0))
	mysql.connection.commit()
	
	
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)
