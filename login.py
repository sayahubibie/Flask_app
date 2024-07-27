from flask import Flask,request,render_template,flash,redirect,url_for

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/form',methods=['GET'])
def form():
    return render_template('login.html')


@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'sayali' and password == '123456':
        return f"You are logged in successfully,{username}"
    else:
        return "Invalid Credentials, please try again"

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            return redirect(url_for('form'))
        else:
            #flash('Registration successfully')
            return redirect(url_for('home'))
    return render_template('register.html')


app.run(debug=True)