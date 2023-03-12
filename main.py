from flask import Flask, render_template, send_file, request, redirect, url_for, session,make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/signin')
def signin():
  return render_template('signin.html')

@app.route('/signout')
def signout():
  return render_template('home.html')

app.run(host='0.0.0.0', port=81)
