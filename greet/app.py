from flask import Flask, request

app = Flask(__name__)

@app.route("/welcome")
def say_welcome():
    """Return simple Welcome greeting."""
    return "welcome"


@app.route("/welcome/home")
def say_welcome_home():
    """Return simple Welcome home greeting."""
    return "welcome home"

@app.route("/welcome/back")
def say_welcome_back():
    """Return simple Welcome back greeting."""
    return "welcome back"