# burgers.py
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def select_all():
    dojos = Dojo.select_all()
    return render_template("index.html", dojos=dojos)

@app.route("/dojos", methods = ["POST"])
def insert():
    data = {
        "location" : request.form["location"]
    }
    Dojo.insert_dojo(data)
    return redirect ("/")


@app.route("/select/<int:iddojos>")
def select(iddojos):

    data = {
        "iddojos": iddojos
    }
    dojo_ninja = Dojo.get_dojos_ninjas(data)
    return render_template("select.html", dojo_ninja=dojo_ninja)

@app.route("/new")
def select_ninja():

    dojos = Dojo.select_all()
    return render_template("ninja.html", dojos=dojos )

@app.route("/create_new", methods = ["POST"])
def insert_ninja():

    dojo_id = request.form["ninja_dojo"]
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojos1_iddojo" : request.form["ninja_dojo"]
    }
    Ninja.insert_ninja(data)
    return redirect (f"/select/{dojo_id}")
