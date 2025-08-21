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

# Select
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', users=data)

# Create
@app.route('/create', methods=['POST'])
def create_user():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO users (patient_name, age, email) VALUES (%s, %s, %s)", (name, age, email))
    mysql.connection.commit()
    cursor.close()
    
    return redirect('/')

# Delete
@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cursor.close()
    return redirect('/')

# Edit
@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    if user:
        return render_template('edit.html', user=user)
    else:
        return "User not found", 404

# Update
@app.route('/update/<int:user_id>', methods=['POST'])
def update_user(user_id):
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']

    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE users 
        SET patient_name=%s, age=%s, email=%s 
        WHERE id=%s
    """, (name, age, email, user_id))
    mysql.connection.commit()
    cursor.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)