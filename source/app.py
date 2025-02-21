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
        mess=request.form['mess']
        con=conn.connection.cursor()
        query="INSERT INTO message(name,email,mess) VALUES (%s,%s,%s)"
        res=con.execute(query,(name,email,mess))
        con.connection.commit()
        con.close()
        return redirect(url_for('home'))
    
    return render_template("contact.html")



@app.route('/login')
def login():
    return render_template("sign up.html")


@app.route('/signup')
def signup():
    if request.method==['GET', 'POST']:
        username=request.form['name']
        password=request.form['pass']
        con=conn.connection.cursor()
        query="SELECT * FROM login user_name= %s AND password= %s"
        res=con.execute(query,(username,password))
        con.connection.commit()
        con.close()


@app.route('/logindata')
def logindata():
    if request.method==['GET', 'POST']:
        username=request.form['name']
        password=request.form['pass']
        con=conn.connection.cursor()
        query="INSERT INTO login(username,password) VALUES (%s,%s)"
        res=con.execute(query,(username,password))
        con.connection.commit()
        con.close()
        
        
    return redirect("home.html")


@app.route('/details')
def detail():
    return render_template("details.html")


@app.route('/booking')
def book():
    return render_template("booking page.html")



if __name__=='__main__':
    app.run(debug=True)