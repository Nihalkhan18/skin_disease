from flask import Flask, render_template, request, session
import psycopg2

app = Flask(__name__)
app.secret_key = "skin"

def connect_to_db():
    return psycopg2.connect(
        user="postgres",
        password="root",
        host="localhost",
        port=5432,
        database="demo_db"
    )
conn= connect_to_db()
cursor= conn.cursor()

@app.route('/add', methods=['POST'])
def add_users():
    name = request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    cursor.execute("""
                INSERT INTO users(username, email, password)
               VALUES(%s,%s,%s)
               """,(name,email,password))
    conn.commit()

    session['id']= cursor.lastrowid 
    session['name']=name
    session['email']=email

    return render_template("successfull.html")

@app.route("/")
def home(): 
    return render_template("index.html")




app.run(debug=True, port=8080)