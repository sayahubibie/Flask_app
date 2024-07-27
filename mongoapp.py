from flask import Flask,request,render_template,redirect,url_for
from pymongo import MongoClient
from bcrypt import hashpw, gensalt

app = Flask(__name__)
# client = MongoClient('mongodb://localhost:27017/')

mongo_uri ="mongodb+srv://sayalishende:sayali%40123@sayalishende.otpu5gi.mongodb.net/?retryWrites=true&w=majority&appName=sayalishende"
#username = sayalidhende
#password = sayali@123 = [sayali%40123]  i.e @= %40 
client = MongoClient(mongo_uri)

db = client['Flask-DB']
collection = db['Users']
collection1 = db['index']

#this for testing in post-man
@app.route('/add_data',methods=['POST'])
def add_data():
    data = request.json
    collection.insert_one(data)

    return 'Data Added to MangoDB'

@app.route('/')
def index():
    return render_template('indexform.html')

@app.route('/submit',methods = ['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hashed_password = hashpw(password,gensalt())

        form_data = {
            'name' : name,
            'email' : email,
            'password' : hashed_password
        }
        collection1.insert_one(form_data)
        return redirect(url_for('index'))



if __name__=="__main__":
    app.run(host=0.0.0.0,port=2001)

#app.run(debug=True)


# for encrypt the password we need  "pip install pymongo bcrypt"