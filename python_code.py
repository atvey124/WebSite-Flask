from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")

def main_str():
    return render_template("basic.html",title = "Главная страница 2.0")


@app.route("/info")
def info():
    return "Информация о сайте"

@app.route("/hello/<name>")

def hello(name):
    return f"Hello {name}"

@app.route("/calc/<int:x>/<int:y>")

def calc(x,y):
    return f"{x} + {y} = {x + y}"

@app.route("/people")

def people():
    
    list_people = ["gf","fdgg","fdg","gdgfd","dgfgd"]
    
    return render_template("people.html",title = "Люди",data = list_people)

@app.route("/comm")
def comm():
    list_comment = ["blyy","gcfg","gfh","gfhg","hfhf"]
    return render_template("comment.html",title = "Комментарии",data = list_comment)
    



if __name__ == "__main__":
    app.run()