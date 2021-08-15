from flask import Flask, redirect, url_for,render_template,request,jsonify
import sqlite3

app = Flask(__name__)

#Our main page
#@app.route("/")
#def home():
#	return "Helloo main page"

#display content from html page to flask page
@app.route("/")
def home():
	return render_template("index.html")

#how to determine whether to use GET or POST for our form
#if the req is POST,(means user is entering his data(name) send that to /usr route)
#else if he just landed on that page, it should be a GET req
@app.route("/login",methods=["POST","GET"])
def login():
	if request.method =="POST":
		user = request.form["nm"]
		return redirect(url_for("user", usr=user))
	else:
		return render_template("login.html")	

	

@app.route("/<usr>")
def user(usr):
	return f"<h1>{usr}</h1>"

#user's name in address
#@app.route("/<name>")
#def user(name):
#	return f"Hello {name}!"

#if user lands on admin page redirect him to homepage
@app.route("/admin")
def admin():
	return redirect(url_for("home"))

if __name__ == "__main__":
	app.run(debug=True)