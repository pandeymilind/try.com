
from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)



@app.route("/signin",methods=["POST","GET"])
def signin():
    return render_template("signin.html")



if __name__=="__main__":
    app.run()
