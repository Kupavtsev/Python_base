# Imported to work!
# import email_validator
# pip install email_validator
# or pip install wtforms[email]

from flask import Flask, request
from flask.json import jsonify
from threading import Lock
from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField, ValidationError
from datetime import datetime

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)

# We check if the current month equal to users Birth month
# This is custom validation method    
def month_check(form, field):
    current_month = datetime.now().month
    users_month = form.data['birth'].month
    if users_month != current_month:
        raise ValidationError('Not Current Month!')

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[
        validators.Length(min=4, max=25)
    ])
    email = StringField(label='E-mail', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    job = StringField(label='JOB', validators=[
        validators.AnyOf(['IT', 'Bank', 'HR'])
    ])
    birth = DateField(label='Date', format='%Y-%m-%d',
     validators=[month_check
    ])


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # print('request.form and data')
        # print(request.form)
        form = ContactForm(request.form)
        status_output = {0:'All Correct', 1: 'Validation Error'}
        # print(form.data)
        # print('form.validate()')
        # print(form.validate())

        # Validation answer
        if form.validate():
            status_check = jsonify(status_output[0])
            return status_check
        else:
            status_check = jsonify(status_output[1])
            error_list = jsonify(form.errors)
            return status_check and error_list

    if request.method == 'GET':
        # return 'hello world!', 200
        return '''
        <form method="post">
            <p><strong>Введите имя пользователя</strong></p>
            <p><input type=text name=name></p>

            <p><strong>Введите E-mail</strong></p>
            <p><input type=text name=email></p>

            <p><strong>Введите работу (IT, Bank or HR)</strong></p>
            <p><input type=text name=job></p>

            <p><strong>Введите дату рождения (Y-M-D)</strong></p>
            <p><input type=text name=birth></p>

            <p><input type=submit value=Login></p>
        </form>
    '''


if __name__ == '__main__':
    app.run()
