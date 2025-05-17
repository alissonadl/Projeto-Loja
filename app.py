from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/termos")
def termos():
    return render_template("termos_de_uso.html")

