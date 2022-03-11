from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    operation = request.form["operation"]
    result = eval(operation)
    return render_template("index.html", result=str(result))

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000)
