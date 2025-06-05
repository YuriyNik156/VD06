from flask import render_template, request, redirect, url_for
from hometask_app import app

queries = []

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        city = request.form.get("city")
        hobby = request.form.get("hobby")
        dish = request.form.get("dish")
        if name and age and city and hobby:
            queries.append({"name" : name, "age" : age, "city" : city, "hobby" : hobby, "dish" : dish})
            return redirect(url_for("index"))
    return render_template("questions.html", queries = queries)