from flask import Flask
# double underscore variable is the name of a module
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"