import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')

# Database config
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

mysql = MySQL(app)

# Routing
@app.route('/')
def index():
    query = mysql.connection.cursor()
    query.execute("SELECT * FROM users")
    data = query.fetchall()
    query.close()
    return render_template('index.html', users=data)


if __name__ == '__main__':
    app.run(debug=True)