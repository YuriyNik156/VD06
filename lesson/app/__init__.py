from flask import Flask

app = Flask(__name__)
app.config["SECRET KEY"] = "you-will-never-guess"

from app import routes
