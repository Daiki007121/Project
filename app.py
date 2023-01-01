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
def hello():

    
    # if 
    # flash("正解を入力してください")
    # return redirect(request.url)

    return render_template("index1.html")


@app.route("/index2", methods=["POST"])
def index2():
    p = request.form["test"]
    if p == "姫待不動尊":
        print(p)
        return render_template("index2.html")
    else:
        flash("正解を入れてください")
        return redirect("/")


# @app.route("/", methods=["GET", "POST"])
# def redirect_to_page():
#      if request.method == "POST":
#          if "file" not in request.files:
#              flash("ファイルが選択されていません")
#              return redirect(request.url)
#          if a = "姫待不動尊"
#             return redirect("index2.html")

@app.route("/index3",methods=["POST"])
def index3():
    p = request.form["test"]
    if p == "神拝詞":
        print(p)
        return render_template("index3.html")
    else:
        flash("正解を入れてください")
        return render_template("/index2.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
