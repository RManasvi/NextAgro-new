from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="Manasvi",
    password="manasvi",
    database="community"
)

mycursor = mydb.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        location = request.form['location']
        crop = request.form['crop']

        query = "INSERT INTO farmers (username, password, location, crop) VALUES (%s, %s, %s, %s)"
        values = (username, password, location, crop)
        mycursor.execute(query, values)
        mydb.commit()

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = "SELECT * FROM farmers WHERE username = %s AND password = %s"
        mycursor.execute(query, (username, password))
        result = mycursor.fetchone()

        if result:
            session['farmer_id'] = result[0]
            session['user_id'] = result[0]
            session['username'] = result[1]
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials!"
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'farmer_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        message = request.form['message']
        query = "INSERT INTO posts (farmer_id, message) VALUES (%s, %s)"
        values = (session['farmer_id'], message)
        mycursor.execute(query, values)
        mydb.commit()

    query = "SELECT farmers.username, farmers.location, posts.message FROM posts JOIN farmers ON posts.farmer_id = farmers.id"
    mycursor.execute(query)
    posts = mycursor.fetchall()

    return render_template('dashboard.html', username=session['username'], posts=posts)

@app.route('/rental')
def rental():
    return render_template('rental.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
