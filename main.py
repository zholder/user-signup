from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("form.html")

def validate_length(validate_param):
    if len(validate_param) > 2 and len(validate_param) <20:
        return True

def is_blank(validate_param):
    if validate_param == '':
        return True

def contains_space(validate_param):
    for char in validate_param:
        if char == ' ':
            return True

def password_match(password, verify_password):
    if password == verify_password:
        return True

def email_check(email):
    if '@' and '.' in email:
        return True

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if is_blank(username) or contains_space(username) or not validate_length(username):
        username_error = 'Username invalid'
    
    if is_blank(password) or contains_space(password) or not validate_length(password):
        password_error = 'Password invalid'

    if is_blank(verify_password):
        verify_password_error = 'Please enter a verification password'
    
    if verify_password != password:
        verify_password_error = 'Password mismatch'

    if not email_check(email):
        email_error = 'Email invalid'

    if validate_length(username) and validate_length(password) and validate_length(verify_password) and verify_password == password:
        return redirect('/success?username={0}'.format(username))

    else:
        return render_template("form.html", username=username, email=email, username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)

@app.route('/success')
def success():
    username = request.args.get('username')
    return render_template("success.html", username=username)


app.run()