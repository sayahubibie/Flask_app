# 1st install :  pip install Flask_Mail

from flask import Flask,json,render_template,request
from flask_mail import *

app = Flask(__name__)

# 2 step verification should be on .....check app password

with open('config.json','r') as f:    # 'r' for reading and 'w' for writting the config.json
    params = json.load(f) ['param']

# setting configuration for sending mail

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = params['gmail-user']
app.config['MAIL_PASSWORD'] = params['gmail-password']
app.config['MAIL_USE_TLS'] = True  #Transport Layer Security
app.config['MAIL_USE_SSL'] = False  #Secured Socket Layer

mail = Mail(app)

@app.route('/')
def mailfunction():
    return render_template('mailform.html')

@app.route('/send_email',methods=['POST'])
def send_mail():
    recipient = request.form['recipient']
    subject = request.form['subject']
    body = request.form['body']
    msg = Message(subject,sender=app.config['MAIL_USERNAME'],recipients=[recipient])
    msg.body = body
    mail.send(msg)

    return 'Message send successfully'

app.run(debug=True)
