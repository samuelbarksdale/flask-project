from flask import Flask, render_template
# double underscore variable is the name of a module
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return "<h1>About Page!<h1>"

if __name__ == '__main__':
    app.run(debug=True)


