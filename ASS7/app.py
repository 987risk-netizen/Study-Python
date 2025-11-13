from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def db():
    return mysql.connector.connect(host='localhost', user='root', password='root', database='event_db')

@app.route('/')
def index():
    event_filter = request.args.get('event', 'ALL')
    
    conn = db()
    c = conn.cursor(dictionary=True)
    
    if event_filter == 'ALL':
        c.execute('SELECT * FROM registrations ORDER BY created_at DESC')
    else:
        c.execute('SELECT * FROM registrations WHERE event=%s ORDER BY created_at DESC', (event_filter,))
    
    data = c.fetchall()
    c.close()
    conn.close()
    
    return render_template('index.html', data=data, selected=event_filter)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
