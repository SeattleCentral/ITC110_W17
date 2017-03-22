import os
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def madlibform():
    return render_template('form.html')

@app.route('/story', methods=['POST'])
def madlibstory():
    context = {
        'noun1': request.form['noun1'],
        'noun2': request.form['noun2'],
        'noun3': request.form['noun3'],
        'noun4': request.form['noun4'],
        'noun5': request.form['noun5'],
        'noun6': request.form['noun6'],
        'noun7': request.form['noun7'],
        'noun8': request.form['noun8'],
        'noun9': request.form['noun9'],
        'noun10': request.form['noun10'],
        'proper_noun1': request.form['proper_noun1'],
        'proper_noun2': request.form['proper_noun2'],
        'verb1': request.form['verb1'],
        'verb2': request.form['verb2'],
        'verb3': request.form['verb3'],
        'verb4': request.form['verb4'],
        'verb5': request.form['verb5'],
        'verb6': request.form['verb6'],
        'verb7': request.form['verb7'],
        'verb8': request.form['verb8'],
        'verb9': request.form['verb9'],
        'verb10': request.form['verb10'],
        'adj1': request.form['adj1'],
        'adj2': request.form['adj2'],
        'adj3': request.form['adj3'],
        'adverb': request.form['adverb']
    }
    return render_template('story.html', context=context)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    host = os.getenv('IP', '0.0.0.0')
    app.run(port=port, host=host)

