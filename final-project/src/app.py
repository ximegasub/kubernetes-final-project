import os
from flask import Flask, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_DATABASE'] = os.getenv("MYSQL_DATABASE")


mysql = MySQL(app)
@app.route('/')
def welcome():
    return "Welcome to the kubernetes final project"

@app.route('/add-employee', methods=['POST'])
def get_add_employee():
    input_data = request.json
    name = input_data.get('name', 'ximena')
    last_name = input_data.get('last_name', 'subieta')
    role = input_data.get('role', 'developer')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if_db = "SHOW DATABASES LIKE 'myappdb'"
    cursor.execute(if_db)
    result = cursor.fetchone()
    if not result:
        create_db = """CREATE DATABASE myappdb"""
        cursor.execute(create_db)
        mysql.connection.commit()
    uses = "USE myappdb"
    cursor.execute(uses)
    if_table = "SHOW TABLES LIKE 'employee'"
    cursor.execute(if_table)
    result = cursor.fetchone()
    if not result:
        create_table = """CREATE TABLE employee (
            id int NOT NULL AUTO_INCREMENT,
            name varchar(255) NOT NULL,
            last_name varchar(255),
            role varchar(255),
            PRIMARY KEY (id)
        )"""
        cursor.execute(create_table)
        mysql.connection.commit()
    cursor.execute('SELECT * FROM myappdb.employee WHERE name = %s',(name,))
    result = cursor.fetchone()
    if result:
        msg = 'Employee already exists'
    else:
        cursor.execute('INSERT INTO myappdb.employee VALUES (NULL, %s, %s, %s)', (name, last_name, role))
        mysql.connection.commit()
        msg = "The employee with name: {}, last name: {}, role: {} was created succesfully.".format(name, last_name, role)
    return msg

if __name__ == "__main__":
    app.run(debug=True)
