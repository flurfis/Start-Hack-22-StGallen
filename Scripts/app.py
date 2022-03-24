from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, World 2.0'

@app.route('/hello/hello2')
def blob():
    return "Blubero"