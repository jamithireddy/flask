# Set up your imports here!
# import ...
from flask import Flask
app = Flask(__name__)


@app.route('/')  # Fill this in!
def index():
    return "<h1>Welcome to the Puppy Latin page.</h1><h1>Head to /puppy_latin/ and enter your puppy name</h1>"
    # Create a generic welcome page.


@app.route('/puppy_latin/<name>')  # Fill this in!
def puppylatin(name):
    if name[-1].lower() == 'y':
        return name[:-1]+'ius'
    else:
        return name+'y'


if __name__ == '__main__':
    app.run()
