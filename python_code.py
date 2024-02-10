
from flask import Flask, render_template
from register import RegisterForm


app = Flask(__name__)

app.config["SECRET_KEY"] = " hello hello  hello hello"

@app.route("/reg", methods = ["GET", "POST"])

def reg():
    form = RegisterForm()
    if form.validate_on_submit:
        print(form.data)
    return render_template("reg.html", form = form)


@app.route("/")

def main():
    return render_template("basic.html", title = "основная страница")

@app.route("/info")

def info():
    return render_template("info.html", title = "Страница с информацией")

@app.route("/people")

def people():
    list_people = ["gfgf","gfhg","ftgf","hgfh","fhfj"]
    return render_template("list_people.html",title = "Страница пользователей",data = list_people)

@app.route("/comm")

def comm():
    list_com = ["dfgfh","gfhg","hfgfh","hfgfh","hffh"]
    return render_template("comment.html", title = "Комментарии",data = list_com)

@app.route("/hello/<name>")

def hello(name):
    return render_template("hello.html", title = "Приветствие",name1 = name)

if __name__ == "__main__":
    app.run()