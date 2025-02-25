from flask import Flask,render_template,redirect,request,url_for,flash
from flask_mysqldb import MySQL,MySQLdb
from twilio.rest import Client
from dotenv import load_dotenv
import os
from sms import main


app = Flask(__name__)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_DB']= "parking"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "Kgkite@123"
app.secret_key="myapp"
conn = MySQL(app)



@app.route('/')
def start():
    return render_template("front page.html")


@app.route('/home')
def home():
    return render_template ('home.html')


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/data',methods=['POST'])
def data():
    if request.method== 'POST':
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        con=conn.connection.cursor()
        query="INSERT INTO message(name,email,mess) VALUES (%s,%s,%s)"
        res=con.execute(query,(name,email,message))
        conn.connection.commit()
        conn.connection.close()
        
        return redirect(url_for('home'))
    
    return render_template("contact.html")



@app.route('/login')
def login():
    return render_template("sign up.html")


@app.route('/signin',methods=['POST'])
def signin():
    if request.method==['GET', 'POST']:
        username=request.form['username']
        ph_no=request.form['phno']
        password=request.form['password']
        con=conn.connection.cursor()
        query="SELECT * FROM login user_name= %s AND phno= %s password= %s"
        res=con.execute(query,(username,ph_no,password))
        conn.connection.commit()
        
        return redirect(url_for("home"))
    
    return redirect(url_for("home")) 
        


@app.route('/signup',methods=['POST'])
def signup():
    if request.method== 'POST':
        username = request.form['username']
        ph_no=request.form['phno']
        password = request.form['password']
        con=conn.connection.cursor()
        query="INSERT INTO login(username,phno,password) VALUES (%s,%s,%s)"
        res=con.execute(query,(username,ph_no,password))
        conn.connection.commit()
        
        return redirect(url_for("home"))
    
    return redirect(url_for("home"))


@app.route('/places')
def places():
    return render_template("places.html")


@app.route('/prozone')
def prozone():
    return render_template("prozone.html")


@app.route('/fun')
def fun():
    return render_template("fun.html")


@app.route('/brookfields')
def brookfields():
    return render_template("brookfields.html")


@app.route('/kg')
def kg():
    return render_template("kg.html")


@app.route('/kmch')
def kmch():
    return render_template("kmch.html")

@app.route('/psg')
def psg():
    return render_template("psg.html")


@app.route('/qr')
def qr():
    return render_template("qr.html")


@app.route('/book',methods=['POST'])
def book():
    if request.method== 'POST':
        slot = request.form['slot']
        subslot=request.form['subslot']
        time = request.form['time']
        main(slot,subslot,time)
        
        return redirect(url_for("home"))
    
    return redirect(url_for("home"))


if __name__=='__main__':
    app.run(debug=True)