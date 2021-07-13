from flask import Flask, request, render_template, flash, redirect, jsonify, session
#from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

responses = 'responses'

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

stored_responses = 'responses'
#memorize[stored_responses] = []

@app.route('/')
def show_survey_title():
    """Shows survey title"""
    return render_template('base.html')

@app.route('/start', methods=['POST'])
def start_survey():
    memorized[stored_responses] = []
    return redirect('/questions/0')

@app.route('/answer', methods=['POST'])
def question_handel():
        return render_template('answer.html')


@app.route('/thanks')
def say_thanks():
    """Thanks user"""
    return render_template('thanks.html')


