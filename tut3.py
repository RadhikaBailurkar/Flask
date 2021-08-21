from flask import Flask, request, render_template
app = Flask(__name__)

from flaskext.mysql import MySQL

#create a db connection with the MySQL database
mysql = MySQL()

#configuring MySQL for the web application
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'organization'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#initialize mysql
mysql.init_app(app)

#create connection to access data
conn = mysql.connect()

@app.route("/")
def index():
	cursor = conn.cursor()
	cursor.execute('select * from employee')
	data = cursor.fetchall()
	return render_template('ttable.html', data=data)

if __name__ == '__main__':
	app.run(debug=True)