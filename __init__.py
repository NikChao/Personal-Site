from flask import Flask, request, render_template
app = Flask(__name__)

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
    
@app.errorhandler(404)
def page_not_found(e):
    return "Sorry mate, no page here, will make this error message prettier next time"

if __name__ == "__main__":
    app.run
