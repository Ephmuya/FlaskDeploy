import flask
from flask import request, jsonify
import smtplib
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.





@app.route('/api/v1/resources/send', methods=['GET'])
def sendmessage():
    name = request.args['name']
    email = request.args['email']
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('email', 'password')
    mail.sendmail('email',email, "This is send using Python " + name)
    mail.close()
    return "Done"

app.run()