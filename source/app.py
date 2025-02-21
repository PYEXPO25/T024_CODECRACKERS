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

@app.route('/data', methods=['POST','GET'])
def data():
    con=conn.connection.cursor(MySQLdb.cursors.DictCursor)
    query="SELECT * FROM user"
    con.execute(query)
    result=con.fetchall()
    con.connection.commit()
    return render_template('add.html',data=result)

@app.route('/sign',methods=['POST','GET'])
def sign():
    return render_template('sign.html')

@app.route('/sign1',methods=['POST','GET'])
def sign1():
    if request.method == 'POST':
        name=request.form['name']
        age=request.form['age']
        place=request.form['place']  
        rollno=request.form['rollno']
        con=conn.connection.cursor(MySQLdb.cursors.DictCursor)
        query="INSERT INTO user (name,age,place,rollno) values (%s,%s,%s,%s)"
        result=con.execute(query,(name,age,place,rollno))
        con.connection.commit()
        con.close()
        return redirect (url_for('data'))
    return render_template('add.html')
    

if __name__=='__main__':
    app.run(debug=True)