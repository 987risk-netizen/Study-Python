from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'abc'

def db():
    return mysql.connector.connect(host='localhost', user='root', password='root', database='event_db')

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username'] == 'admin' and request.form['password'] == 'admin':
        session['user'] = 'admin'
        return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    
    conn = db()
    c = conn.cursor(dictionary=True)
    
    if request.args.get('del'):
        c.execute('DELETE FROM registrations WHERE id=%s', (request.args.get('del'),))
        conn.commit()
    
    c.execute('SELECT * FROM registrations')
    data = c.fetchall()
    
    edit = None
    if request.args.get('edit'):
        c.execute('SELECT * FROM registrations WHERE id=%s', (request.args.get('edit'),))
        edit = c.fetchone()
    
    c.close()
    conn.close()
    return render_template('dashboard.html', data=data, edit=edit)

@app.route('/save', methods=['POST'])
def save():
    if 'user' not in session:
        return redirect('/login')
    
    f = request.form
    conn = db()
    c = conn.cursor()
    
    if f.get('id'):
        c.execute('UPDATE registrations SET name=%s,email=%s,mobile=%s,event=%s,password=%s WHERE id=%s',
                  (f['name'], f['email'], f['mobile'], f['event'], f['password'], f['id']))
    else:
        c.execute('INSERT INTO registrations (name,email,mobile,event,password) VALUES (%s,%s,%s,%s,%s)',
                  (f['name'], f['email'], f['mobile'], f['event'], f['password']))
    
    conn.commit()
    c.close()
    conn.close()
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
