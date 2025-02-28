from flask import Flask,render_template,redirect,request,url_for,flash,jsonify
from flask_mysqldb import MySQL,MySQLdb
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime, timedelta
from sms import main


app = Flask(__name__)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_DB']= "parking"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "Kgkite@123"
app.secret_key="myapp"
conn = MySQL(app)

name=""
ph_no=0
password=""



@app.route('/')
def start():
    alerts = fetch_alerts()
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
        query="SELECT * FROM login WHERE user_name= %s AND phno= %s password= %s"
        con.execute(query,(username,ph_no,password))
        user = con.fetchone()
        if user:
            
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


@app.route('/entryexit')
def entryexit():
    con=conn.connection.cursor()
    query="SELECT * FROM entryexit"
    con.execute(query)
    logs = con.fetchall()
    return render_template('entry.html', logs=[{'numplate': log[0], 'entry_time': log[1], 'exit_time': log[2]} for log in logs])

@app.route('/entry', methods=['POST'])
def entry():
    numplate = request.form['numplate']
    entry_time = datetime.now()
    con=conn.connection.cursor()
    con.execute("INSERT INTO entryexit (numplate, entry_time) VALUES (%s, %s)", (numplate, entry_time))
    conn.connection.commit()
    return redirect('/entryexit')

@app.route('/exit', methods=['POST'])
def exit():
    numplate = request.form['numplate']
    exit_time = datetime.now()
    con=conn.connection.cursor()
    con.execute("UPDATE entryexit SET exit_time = %s WHERE numplate = %s AND exit_time IS NULL", (exit_time, numplate))
    conn.connection.commit()
    return redirect('/entryexit')


@app.route('/book',methods=['POST'])
def book():
    if request.method== 'POST':
        slot = request.form['slot']
        subslot=request.form['subslot']
        time = request.form['time']
        mess=f'Your have booked you parking on {slot} slot {subslot} at Time:{time}'
        print(mess)
        main(mess)
        con=conn.connection.cursor()
        query="INSERT INTO book(slot,subslot,book_time) VALUES (%s,%s,%s)"
        res=con.execute(query,(slot,subslot,time))
        conn.connection.commit()
        
        
        return redirect(url_for("qr"))
    
    return redirect(url_for("home"))


def fetch_alerts():
    """Fetch reservations starting in the next 10 minutes."""
    alerts = []
    try:
        con = conn.connection.cursor()

        now = datetime.now()
        alert_time = now + timedelta(minutes=10)

        # Fetch bookings
        con.execute("SELECT slot, subslot, time FROM reservations")
        bookings = con.fetchall()

        for slot, subslot, start_time in bookings:
            booking_time = datetime.strptime(str(start_time), "%H:%M:%S")

            # If booking is within the next 10 minutes, add to alerts
            if now.hour == booking_time.hour and (booking_time.minute - now.minute) <= 10:
                message=f"🚨 ALERT: Slot {slot}, Subslot {subslot} starts at {start_time}!"
                alerts.append(message)
                main(message)

        conn.close()
    except Exception as err:
        alerts.append(f"❌ Database Error: {err}")
    
    return alerts


if __name__=='__main__':
    app.run(debug=True)