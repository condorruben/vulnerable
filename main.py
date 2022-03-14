from flask import Flask, render_template, redirect, abort, url_for, make_response
from flask import request
import os
import sys
import subprocess
import time
import random

app = Flask(__name__)

@app.route("/")
def index():
    r = make_response(render_template("index.html"))
    r.headers["Server"] = "flask, nginx/1.18.0 (Ubuntu)"
    return r

@app.route("/calculate", methods=["POST"])
def calculate():
    fail_proba = 10

    if random.choices([True, False], weights=(fail_proba, 100 - fail_proba))[0]:
        choice = random.choices(['abort', 'redirect', 'sleep', 'redirect_inf', 'exception'])[0]
        if choice == "abort":
            return abort(403)
        elif choice == "redirect":
            return redirect("http://somethingwentwrong")
        elif choice == "sleep":
            time.sleep(60 * 2)
        elif choice == "redirect_inf":
            return redirect(url_for("redirect_inf"))
        elif choice == "exception":
            raise Exception()

    operation = request.form["operation"]
    result = eval(operation)
    r = make_response(render_template("index.html", result=str(result)))
    r.headers["Server"] = "flask, nginx/1.18.0 (Ubuntu)"
    return r

@app.route("/redirect_inf")
def redirect_inf():
    return redirect(url_for("redirect_inf"))

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000)
