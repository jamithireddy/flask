from crypt import methods
from flask import Flask, render_template, redirect, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app = Flask(__name__)
app.config['SECRET_KEY'] = "mysecretkey"


class info(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    email = StringField("Enter your email")
    enrolled = BooleanField("Have you already enrolled to the course?")
    education = RadioField("Please select your education level", choices=[('graduation', 'Graduation'), (
        'bachelors', 'Bachelors Degree'), ('masters', 'Masters Degree'), ('doctors', 'PHd and above')])
    diet = SelectField("Please select your Food Preferece", choices=[('vegan', 'Vegan'), (
        'veggie', 'Vegitarian'), ('chic', 'Chicken Only'), ('nopork', 'No Pork'), ('nobeef', 'No Beef')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = info()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['enrolled'] = form.enrolled.data
        session['education'] = form.education.data
        session['diet'] = form.diet.data

        return redirect(url_for('thankyou'))
    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)
