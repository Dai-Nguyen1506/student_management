# app/__init__.py
from flask import Flask, redirect, url_for
from app.routes import student_bp
from dotenv import load_dotenv
from os import path

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = "abc123"

    # register blueprint
    app.register_blueprint(student_bp)

    # route gốc "/" → redirect sang /students
    @app.route("/")
    def home():
        return redirect(url_for("students.index"))

    return app
