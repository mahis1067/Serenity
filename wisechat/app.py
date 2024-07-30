from flask import Flask, jsonify, redirect, render_template, request, url_for, session

from openai import OpenAI
"""
from dotenv import load_dotenv, dotenv_values

load_dotenv()



connection = OpenAI()

"""

app = Flask(__name__)
app.secret_key = 'your_secret_key' 


users = {}
is_logged_in = False  
"""

@app.route ('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        print (prompt)
        return render_template("index.html")
    else:
        return render_template("index.html")
"""

@app.route('/')
def index():
    global is_logged_in
    if is_logged_in:
        return redirect(url_for('home'))
    return redirect(url_for('sign'))



@app.route('/home')
def home():
    name = session.get('name', 'Guest')  
    return render_template('home.html', name=name)

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    global is_logged_in
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        if username and password and name:
            users[username] = {'password': password, 'name': name}
            session['name'] = name  
            is_logged_in = True
            return redirect(url_for('home'))
    return render_template('sign.html')

@app.route('/text')
def text():
    return render_template('test.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    
    response = user_input
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
