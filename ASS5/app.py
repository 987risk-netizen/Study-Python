from flask import Flask, render_template, request, flash, redirect, send_from_directory
import mysql.connector

app = Flask(__name__, static_folder='static')
app.secret_key = 'your_secret_key'

def get_db():
    return mysql.connector.connect(host='localhost', user='root', password='root', database='event_db')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/')
def home():
    return redirect('/registration')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO registrations (name, email, mobile, event, password) VALUES (%s, %s, %s, %s, %s)",
                       (request.form['name'], request.form['email'], request.form['mobile'], request.form['event'], request.form['password']))
        db.commit()
        cursor.close()
        db.close()
        flash('Registration Done!')
        return redirect('/registration')
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True)
