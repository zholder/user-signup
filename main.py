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

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']

    username_error = ''
    password_error = ''
    verify_password_error = ''

    if is_blank(username):
        username_error = 'Please enter a username'
    
    if is_blank(password) or contains_space(password):
        password_error = 'Password invalid'

    if is_blank(verify_password):
        verify_password_error = 'Please enter a verification password'
    
    if verify_password != password:
        verify_password_error = 'Password mismatch'

    # if not is_blank(password) and not contains_space(password) and not is_blank(verify_password):
    #     if password_match(password, verify_password):
    #         verify_password_error = 'Passwords do not match'

    if validate_length(username) and validate_length(password) and validate_length(verify_password) and verify_password == password:
        return redirect('/success?username={0}'.format(username))

    else:
        return render_template("form.html", username=username, username_error=username_error, password_error=password_error, verify_password_error=verify_password_error)

@app.route('/success')
def success():
    username = request.args.get('username')
    return render_template("success.html", username=username)



app.run()