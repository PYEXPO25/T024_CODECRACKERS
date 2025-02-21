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

@app.route('/login')
def login():
    return "login"


@app.route('/details')
def detail():
    return "details"

@app.route('/booking')
def book():
    return "booking"


if __name__=='__main__':
    app.run(debug=True)