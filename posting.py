from flask import Flask, render_template,request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

def add_job(company, position, salary, location, remote, qualifications, contact):
    conn = sqlite3.connect('jobs.db')
    c = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO jobs (company, position, salary, location, remote, qualifications, contact, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (company, position, salary, location, remote, qualifications, contact, date))
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('post_job.html')

@app.route('/add_job', methods=['POST'])
def add_job_route():
    company = request.form['company']
    position = request.form['position']
    salary = request.form['salary']
    location = request.form['location']
    remote = request.form['remote']
    qualifications = request.form['qualifications']
    contact = request.form['contact']
    add_job(company, position, salary, location, remote, qualifications, contact)
    return redirect('/')

if __name__ == '__main__':
    app.run(port=1436)
