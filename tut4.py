#Basic Login Page
#https://www.youtube.com/watch?v=R-hkzqjRMwM&t=359s

from flask import Flask,request, render_template, redirect
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("login1.html")

database = {'radhika':'123@radz','bhakti':'art@123'}



@app.route("/form_login", methods=["GET","POST"] )
def login():
	if (request.method == "POST"):
		uname = request.form['username']
		pwd = request.form['password']
		if uname not in database:
			return render_template("login1.html", info="Invalid User")
		else:
			if database[uname]!=pwd:
				return render_template("login1.html", info="Invalid Password")
			else:
				return render_template("home.html", name=uname)
			
	


#@app.route("/sucess")
#def sucess():
#	return <h1 align = "center"> Welcome</h1>


if __name__ == "__main__":
	app.run(debug=True)