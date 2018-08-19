from flask import Flask, render_template
# double underscore variable is the name of a module
app = Flask(__name__)

posts = [
    {
       'author': 'Samuel Barksdale',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Bri Watson',
        'title': 'My First blog post',
        'content': 'Sam is amazing',
        'date_posted': 'April 25, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

