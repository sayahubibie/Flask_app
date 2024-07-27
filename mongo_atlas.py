from flask import Flask , request,render_template,url_for,redirect
from pymongo import MongoClient
from bcrypt import gensalt,hashpw

app = Flask(__name__)

mongo_uri ="mongodb+srv://sayalishende:sayali%40123@sayalishende.otpu5gi.mongodb.net/?retryWrites=true&w=majority&appName=sayalishende"
client = MongoClient(mongo_uri)

db = client['Flask-DB']
collection =db['index']

@app.route('/')
def add():
    return render_template('registration.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        #password = request.form['password'].encode('utf-8')
        #hashed_password = hashpw(password,gensalt())

        form_data = {
            'name' : name,
            'email' : email,
            'password' : password
        }
        collection.insert_one(form_data)
        return redirect(url_for('add'))




app.run(debug=True)