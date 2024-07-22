from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="",
    user="",
    password="",
    database=""
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    lastname = request.form['lastname']
    age = request.form['age']
    term = request.form['term']

    cursor = db.cursor()
    sql = "INSERT INTO users (name, lastname, age, term) VALUES (%s, %s, %s, %s)"
    values = (name, lastname, age, term)
    cursor.execute(sql, values)
    db.commit()

    return render_template('home.html')

@app.route('/get_data')
def get_data():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    
    users = []
    for row in data:
        user = {
            'id': row[0],
            'name': row[1],
            'lastname': row[2],
            'age': row[3],
            'term': row[4]
        }
        users.append(user)

    return render_template('data.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        
        if username == 'admin' and password == 'pass':
            return redirect('/get_data')
        else:
            return render_template('login.html', error='نام کاربری یا رمز عبور اشتباه است.')
    
    return render_template('login.html')