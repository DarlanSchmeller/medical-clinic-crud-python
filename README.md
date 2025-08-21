# 🏥 Medical Clinic - Flask CRUD App

This project it's a very simple web application developed for study, which allows for basic management of patient records in a medical clinic. It uses **Python (Flask)** for the backend and **MySQL** for the database.

---

## 📋 Features

- **Create** new patient records
- **Read** and list all patients
- **Update** existing patient information
- **Delete** patient records

---

## 🛠 Technologies Used

- Python 3
- Flask
- MySQL
- Flask-MySQLdb
- HTML (Jinja2 templates)
- dotenv for environment variables

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone git@github.com:DarlanSchmeller/medical-clinic-crud-python.git
cd medical-clinic-crud
```

### 2. Create and configure the .env file

Create a .env file in the project root with the following content:

```
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=root
MYSQL_DB=medical-clinic
```

⚠️ Make sure MySQL is installed and running on your system.

### 3. Set up the MySQL database

Import the existing schema from the SQL dump file located in the `/database` folder:

```
mysql -u <username> -p < database/main_schema.sql
```

### 4. Install dependencies

Use pip to install the required packages:

```
pip install flask flask-mysqldb python-dotenv
```

### 5. Run the Flask application
```
python app.py
```


### Access the app
Visit http://localhost:5000 in your browser.

---

## ✅ CRUD Endpoints Overview

| Route               | Method | Description                  |
|---------------------|--------|------------------------------|
| `/`                 | GET    | List all users               |
| `/create`           | POST   | Add a new user               |
| `/edit/<user_id>`   | GET    | Load edit form for a user    |
| `/update/<user_id>` | POST   | Update an existing user      |
| `/delete/<user_id>` | POST   | Delete a user                |

---

## 🎓 Purpose

This project was created as part of a college assignment to demonstrate a basic CRUD web application using Python and MySQL. It helps to understand how Flask interacts with databases and handles routing, templates, and form submissions.
