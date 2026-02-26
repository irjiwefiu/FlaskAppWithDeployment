from flask import Flask,render_template,request
from markupsafe import escape

from log import createLogger
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def home():
    logger.info("Home page accessed")
    return render_template('index.html')

@app.route('/about',methods=['POST'])
def about():
    name=request.form['name']
    email=request.form['email']
    message=request.form['message']
    logger.info(f"Received message from {name} with email {email}")
    return f"Thank you for reaching out, <h3>{escape(name)}</h3>! Your message has been received. We will get back to you at <h3>{escape(email)}</h3> as soon as possible. Your Message: <h3>{escape(message)}</h3>"

if __name__=='__main__':
    date= datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    logger=createLogger(date)
    logger.info("Starting Flask app")
    app.run(debug=True,use_reloader=False)




