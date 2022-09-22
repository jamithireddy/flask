from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    mylist = [3, 7, 4, 9, 2, 5]
    return render_template('test.html', mylist=mylist)


if __name__ == '__main__':
    app.run()
