from flask import Flask, request, render_template, flash, redirect
#from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey


#memorize[stored_responses] = []
# stored_responses = 'responses'
responses = []
stored_responses = 0

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



@app.route('/')
def show_survey_title():
    return render_template('start.html')
    
    
@app.route('/start')
def start_survey():
    """Shows """
    return render_template('start.html', survey=survey)
 
    # return redirect('/questions/0')
    # instructions = survey.instructions    
    # title =survey.questions
    # if(len(responses) == len(survey.questions)):
    #     redirect('/questions/0')
    # else:
    #     return render_template('start.html', instructions=instructions, title=title)



# @app.route('/question/<int:qid>')
# def question_handle(qid):
#         return render_template('answer.html')

# @app.route('/thanks')
# def thank_user():
#     return render_template('thanks.html')
        
