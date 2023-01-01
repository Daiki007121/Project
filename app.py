from flask import Flask
from flask import render_template
from flask import request
import json
import requests
import secrets
from flask import redirect, flash

app = Flask(__name__)

# セッション情報を暗号化するためのキー設定
app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def index():

    
    # if 
    # flash("正解を入力してください")
    # return redirect(request.url)

    return render_template("q1.html")


@app.route("/q2", methods=["POST"])
def q2():
    p = request.form["test"]
    if p == "姫待不動尊":
        print(p)
        return render_template("q2.html")
    else:
        flash("正解を入れてください")
        return redirect("/")



@app.route("/q3",methods=["POST"])
def q3():
    p = request.form["test"]
    if p == "神拝詞":
        print(p)
        return render_template("q3.html")
    else:
        flash("正解を入れてください")
        return render_template("q2.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
