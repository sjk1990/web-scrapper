from flask import Flask, render_template, request

app = Flask("WebScrapper")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    keyword = request.args.get("keyword")
    return render_template("report.html", searchingBy=keyword)


app.run(host="127.0.0.1")
