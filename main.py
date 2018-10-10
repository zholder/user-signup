from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    return render_template("success.html", username=username)

app.run()