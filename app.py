from flask import Flask, request, render_template, flash, redirect
#from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey, surveys


#memorize[stored_responses] = []
# stored_responses = 'responses'
responses = []
stored_responses = 0

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)



# @app.route('/')
# def show_survey_title():
#     return render_template('start.html')



@app.route('/')
def show_survey():
    return render_template('base.html')
    
    
@app.route('/start')
def start_survey():
    """Shows """
    if len(responses) == len(survey.questions):
        return redirect('/questions/0')
    title = survey.title
    instructions = survey.instructions
    return render_template('start.html', title=title, instruction=instructions)

@app.route('/answer', methods=['POST'])
def handle_answer():
    choice = request.form['answer']
    responses = stored_responses
    responses.append(choice)
    stored_responses = responses
    if (len(responses) == len(survey.questions)):
        return redirect('/thanks')
        return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:qid>')
def show_questions(qid):
    # if len(responses) == len(survey.questions):
    #     redirect('/thanks')
    # if qid == 0 and len(responses) == 0:
    #     # print('if',responses, qid, len(responses))
    #     question = survey.questions[qid]
    #     prompt = question.question
    #     choices = question.choices
        return render_template('questions.html')




@app.route('/thanks')
def thank_user():
    return render_template('thanks.html')
        
