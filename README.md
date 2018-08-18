# flask-project

# **Steps to setting up Flask**

1. pip install flask
  - Double check by opening python and typing "import flask"
2. Create a file called `flask-blog.py` as a sample code. 
  - copy the code from `http://flask.pocoo.org/`
  - in terminal, `export FLASK_APP=flaskblog.py`
  - `flask run`
  - copy the address and paste it into the URL bar

# **Live Editing**
With the current settings, the you will need to restart flask and run it again in order to see changes. 
In terminal, `export FLASK_DEBUG=1`
`flask run`

# Running Script with python**
add this to `flaskblog.py`
```
if __name__ == '__main__':
  app.run(debug=True)
```  
This allows you to run the scripts as `python flaskblog.py`  
