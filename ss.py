from flask import Flask,render_template


app = Flask(__name__)

@app.route('/')
def login():
    return render_template('s1.html')

@app.route('/register')
def account():
    return render_template('s2.html')


app.run(debug = True)