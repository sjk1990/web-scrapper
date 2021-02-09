from flask import Flask, render_template, request, redirect

import sys

sys.path.append("../scrapper")
from so import get_jobs

app = Flask("WebScrapper")

# fake db
db = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/report")
def report():
    keyword = request.args.get("keyword")
    existingJobs = db.get(keyword)
    if keyword:
        keyword.lower()
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs(keyword)
            # db key & value
            db[keyword] = jobs
    else:
        return redirect("/")
    return render_template("report.html", searchingBy=keyword, resultNumber=len(jobs), jobs=jobs)


@app.route("/export")
def export():
    # if fail try, run except
    try:
        keyword = request.args.get("keyword")
        if not keyword:
            # insidoe of try block, exception is called, then go to except and return redirect
            raise Exception()
        keyword = keyword.lower()
        jobs = db.get(keyword)
        if not jobs:
            raise Exception()
        return f"Generate CSV for {keyword}"
    except:
        return redirect("/")


app.run(host="127.0.0.1")
