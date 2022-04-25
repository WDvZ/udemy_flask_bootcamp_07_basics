from cmath import log
from distutils.log import debug
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1>Generic Welcome Page</h1>'

@app.route('/puppy/<name>')
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"

    last_letter = name[len(name)-1]
    if last_letter.upper() != "Y":
        name_puplatin = name + "y"
    else:
        name_puplatin = name[0:(len(name)-1)] + "iful"
    return '<h1>{}</h1>'.format(name_puplatin)

if __name__ == '__main__':
    app.run(debug=True)
