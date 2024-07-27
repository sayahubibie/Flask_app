# 1st install :  pip install Flask_Mail

from flask import Flask,json
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

@app.route("/")
def index():
    msg = Message("Import Mail",
                  sender = app.config['MAIL_USERNAME'],
                  recipients = ['shyamli.hanvate57@gmail.com','ankitadhakate29@gmail.com','agasheachal09@gmail.com'])
    msg.body = "This is to inform you that... you got shortlisted for next interview round"
    #mail.send(msg)
    with app.open_resource(r"C:\Users\DeLL\OneDrive\Desktop\simple python\armstrong.py","rb") as fp:
        msg.attach(r"C:\Users\DeLL\OneDrive\Desktop\simple python\armstrong.py","application/pdf",fp.read()) 
    mail.send(msg)
    return "Message sent successfully"



app.run(debug=True)