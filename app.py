from flask import Flask, request, render_template, flash, redirect, session
#from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey, surveys


# stored_responses = 'responses'
# responses = []
stored_responses = 0

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def show_survey():
    """ Root route shows base page """
    return render_template('start.html')
    
    
@app.route('/start', methods=['POST'])
def start_survey():
    """Shows survey title and instructions """
    session[stored_responses] = []
    return redirect('/questions/0')

@app.route('/answer', methods=['POST'])
def handle_answer():
    choice = request.form['answer']
    responses = session['stored_responses']
    responses.append('choice')
    session['stored_responses'] = responses

    if (len(responses) == len(survey.questions)):
        return redirect('/thanks')
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:qid>')
def show_questions(qid):
    responses = session.get(stored_responses)
    if(responses is None):
        return redirect('/')
        
    if(len(responses) == len(survey.questions)):
        return redirect('/thanks')
        """Redirects user if they try to manually change url"""
    if(len(responses) != qid):
        flash(f"Invalid question id: {qid}.")
        return redirect(f"/questions/{len(responses)}")
    
    question = survey.questions[qid]
    return render_template(
        "questions.html", question_num=qid, question=question)


@app.route('/thanks')
def thank_user():
    return render_template('thanks.html')