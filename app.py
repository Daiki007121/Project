from flask import Flask
from flask import render_template
from flask import request
import json
import requests
import secrets
from flask import redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///Test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True

# セッション情報を暗号化するためのキー設定
app.secret_key = secrets.token_urlsafe(32)

db = SQLAlchemy(app)

class Quiz(db.Model):
    __tablename__ = 'Quiz'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)

@app.before_first_request
def init():
    db.create_all()

@app.route('/create_question', methods=['GET'])
def question_form():

    return render_template('create_question.html')

@app.route('/create_question', methods=['POST'])
def insert_question():

    question_str = request.form['question']
    answer_str = request.form['answer']
    dbs = Quiz(question=question_str, answer=answer_str)

    db.session.add(dbs)
    db.session.commit()

    return render_template('create_question.html')


@app.route("/")
def index():

    return render_template("q1.html")


@app.route("/answer", methods=["GET"])
def view_question():
    answer_flag = False
    q = db.session.query(Quiz).first()
    #print(q,q.question)
    ids = q.id
    quesion = q.question

    return render_template("answer.html",answer_flag=answer_flag,question=quesion,idx=ids)


@app.route("/answer", methods=["POST"])
def answer():

    q = request.form["question"]
    p = request.form["answer"]
    ids = int(request.form["idx"])

    
    d = db.session.query(Quiz).filter_by(question=q).first()

    if p == d.answer:
        ids += 1
        answer_flag = True
        d = db.session.query(Quiz).filter_by(id=ids).first()
        quesion = d.question
        return render_template("answer.html",answer_flag=answer_flag,question=quesion,idx=ids)
    else:
        flash("正解を入れてください")
        return redirect("/answer")


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
