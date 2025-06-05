from flask import renser_template, request, redirect, url_for
from app import app

queries = []

@app_route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        name = request.form.get("name")
        