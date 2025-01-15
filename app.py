from flask import Flask
from flask import render_template, request

app = Flask(_name_)

@app.route("/")
def index():
    return(render_template("index.html"))

if _name_ == "_main_":

    