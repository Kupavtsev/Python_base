"""
https://en.wikipedia.org/wiki/Singleton_pattern
"""

from flask import Flask, request, url_for
from flask_wtf import FlaskForm
from wtforms import DecimalField, validators
import random

import config

__author__ = 'Oleg Kupavtsev'

class Storage(object):

    number = None

    def __new__(cls):
        if Storage.number is None:
            Storage.number = object.__new__(cls)
        return Storage.number

    @classmethod
    def new_number(cls, limit):
        cls.number = random.randint(1, limit)
        print('Guess this number: ', cls.number)


class GuessForm(FlaskForm):
    guess_form = DecimalField(label='guess_num', validators=[validators.Required()])

app = Flask(__name__)
app.config.from_object(config)

@app.route('/', methods=['GET'])
def home():
    number = Storage()
    number.new_number(100)
    return 'Check it!'


@app.route('/guess', methods=['POST'])
def guess():
    if Storage.number == None:
        return 'You did guess the number'
    
    if request.method == 'POST':
        form = GuessForm(request.form)
        print(form.data)
        if form.validate():
            user_number = form.guess_form.data
            if user_number == Storage.number:
                Storage.new_number(100)
                return 'You did guess my number!'
            elif user_number > Storage.number:
                return 'More than you need'
            elif user_number < Storage.number:
                return 'Less than you need'
        else:
            return str(form.errors)
        # return 'AHA'
    
    else:
        return url_for('home')


if __name__ == '__main__':
    app.run()

