# udemy_flask_bootcamp_07_basics
Python and Flask Bootcamp - Section 7: Flask Basics

# Basic Steps, since I'm going to forget a couple of times

## Code starter

```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Home Page</h1>'

@app.route('/information')
def info():
    return '<h1>on the /information page</h1>'

if __name__ == '__main__':
    app.run()
```

## git and venv

```ps
py -m venv .venv
.venv\scripts\activate
```