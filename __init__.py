import datetime
from flask import Flask, flash, request, render_template
from roster import *

app = Flask(__name__)

@app.route('/ironside')
def ironside():
    try:
        return render_template("ironside.html")
    except Exception, e:
        return str(e)

@app.route('/chezdex')
def chezdex():
    try:
        return render_template("chezdex.html")
    except Exception, e:
        return str(e)

@app.route('/')
def homepage():
    try:
        return render_template("index.html")
    except Exception, e:
        return str(e)

@app.route('/blogs')
def blog_hub():
    try:
        return render_template("blog_hub.html")
    except Exception, e:
        return str(e)

@app.route('/rostering')
def rostering():
    try:
        return render_template("rostering.html", DAYS = days)
    except Exception, e:
        return str(e)


@app.route('/rostering', methods=["POST","GET"])
def add_man():

    fn = request.form['first_name']
    ln = request.form['last_name']
    tp = request.form['telephone']
    day = request.form.get('day')
    multisession = request.form.getlist('multisession')

    for s in multisession:
	s = int(s)
        if len(days[day][s]) < 8:
            days[day][s].append([fn,ln,tp])
            flash('added')
        else:
            flash('that session is full')

    return render_template("rostering.html", DAYS=days)


@app.errorhandler(404)
def page_not_found(e):
    return "Sorry mate, no page here, will make this error message prettier next time"


if __name__ == "__main__":
    app.run
