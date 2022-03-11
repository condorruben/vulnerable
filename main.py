from flask import Flask, render_template, redirect, abort, url_for
from flask import request
import os
import sys
import subprocess
import time
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    if random.choices([True, False], weights=(30, 70))[0]:
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
    return render_template("index.html", result=str(result))

@app.route("/redirect_inf")
def redirect_inf():
    return redirect(url_for("redirect_inf"))

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000)
