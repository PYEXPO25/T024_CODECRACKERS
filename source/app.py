from flask import Flask,render_template,redirect,request,url_for,flash
from flask_mysqldb import MySQL,MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_DB']= "parking"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "Kgkite@123"
app.secret_key="myapp"
conn = MySQL(app)

@app.route('/')
def home():
    return render_template ('home.html')

@app.route('/data')
def data():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        msg=request.form['message']
        con=conn.connection.cursor()
        query="inert into message(name,email,mess) values(%s,%s,%s)"
        res=con.execute(query,(name,email,msg))
        con.connection.commit()
        con.close()
    
     return redirect(url_for('/'))

@app.route('/login')
def login():
    if request.method=="POST":
        username=request.form['name']
        password=request.form['pass']
        con=conn.connection.cursor()
        query="insert into login(username,password) values(%s,%s)"
        res=con.execute(query,(username,password))
        con.connection.commit()
        con.close()

    return render_template("login.html")


@app.route('/details')
def detail():
    return "details"

@app.route('/booking')
def book():
    return "booking"


if __name__=='__main__':
    app.run(debug=True)