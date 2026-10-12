from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/childhood")
def childhood():
    return render_template("childhood.html")

@app.route("/inventions")
def inventions():
    return render_template("inventions.html")

app.run(debug=True)
