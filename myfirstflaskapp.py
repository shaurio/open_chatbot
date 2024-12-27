from os import write

from flask import Flask, request, jsonify
from markupsafe import escape
from flask import render_template
from chatppt import pat_ppt
import uuid


app = Flask(__name__)

with open('chathist.txt', 'w') as file:
    pass

@app.route('/hello/')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>', methods=['GET', 'POST'])
def hello(name=None, age=None):
    show_toast = False
    question = ''

    if request.method == 'POST':
        question = request.form.get('question')
        # response = pat_ppt(question)
        response = pat_ppt(question)
        show_toast = True
        return jsonify({'response': response, "question": question})

    else:
        response = "Ask away!"

    #response = pat_ppt("whats up, how tall is the eiffeil tower")

    person_type = "person"
    if age:
        age = int(age)


        if age < 14:
            person_type = "baby"
        elif 14 < age < 18:
            person_type = "teen"
        else:
            person_type = "adult"


    ctx = {
        "name": name.capitalize(),
        "age": age,
        "type": person_type,
        "response": response,
        "question": question,
        "show_toast": show_toast
    }
    return render_template('hello.html', **ctx)



@app.route('/')
def index():
    # show the user profile for that user
    return f'User'

@app.route('/privacy')
def privacy():
    # show the post with the given id, the id is an integer
    return ('<h1> Welcome to our privacy page. </h1>'
            '<p>Visit our about me!</p>')

@app.route('/about')
def about():
    # show the subpath after /path/
    return ('<h1> Welcome to our about page. </h1>'
            '<p>Nothing to see here. Visit our privacy page!</p>')

@app.route('/clear_chat_hist')
def clear_chat_hist():

    with open('chathist.txt', 'w') as file:
        pass
    return 'success'

