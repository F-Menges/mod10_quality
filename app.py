"""This is a simple Flask application that returns 'hello world'"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit_name", methods=["POST"])
def display_name():
    print("in display_name function")
    if request.method == "POST":
        print("in post method")
        form = request.form
        print("extracted form data")
        print(form)
        user_name = form["my_name"]
        print(user_name)
        return "done"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
