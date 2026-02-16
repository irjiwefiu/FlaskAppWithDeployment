from flask import Flask,render_template,request
from markupsafe import escape

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user',methods=['POST'])
def user():
    name=request.form['name']
    email=request.form['email']
    message=request.form['message']
    return f"Thank you for reaching out, {escape(name)}! Your message has been received. We will get back to you at {escape(email)} as soon as possible. Your Message: {escape(message)}"

if __name__=='__main__':
    app.run(debug=True)




