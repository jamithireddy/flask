from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    username = request.args.get('username')
    for char in username:
        k = char.islower()
        if k == True:
            a = True
            break
        else:
            a = False
    for char in username:
        k = char.isupper()
        if k == True:
            b = True
            break
        else:
            b = False
    for char in username:
        k = char.isnumeric()
        if k == True:
            c = True
            break
        else:
            c = False
    if a == True and b == True and c == True:
        return render_template('report.html', username='Congratulations '+username+' has been created!')
    else:
        return render_template('report.html', username='The username  doesnt  meet the Criteria')


if __name__ == '__main__':
    app.run(debug=True)
