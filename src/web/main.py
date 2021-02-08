from flask import Flask

app = Flask("WebScrapper")


@app.route("/")
def home():
    return "Hello Welcome to Flask"


app.run(host="0.0.0.0")
