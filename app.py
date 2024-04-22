from flask import Flask, render_template, redirect
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS jobs 
                 (id INTEGER PRIMARY KEY, company TEXT, position TEXT, 
                 salary TEXT, location TEXT, remote TEXT, qualifications TEXT, 
                 contact TEXT, date TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    create_table()
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM jobs ORDER BY date DESC")
    jobs = c.fetchall()
    conn.close()
    return render_template('index.html', jobs=jobs)

@app.route('/internships')
def intern():
    create_table()
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM jobs WHERE position = 'Intern' ORDER BY date DESC")
    jobs = c.fetchall()
    conn.close()
    return render_template('index.html', jobs=jobs)

@app.route('/post')
def post_job():
    return redirect('http://127.0.0.1:1436/')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/terms_conditions')
def terms_conditions():
    return render_template('terms_conditions.html')

if __name__ == '__main__':
    app.run(port = 8143, debug=True)
