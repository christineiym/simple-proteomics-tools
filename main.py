"""Running website as package.

To run the website from source code after installing requirements (may need to rename main to be __init__.py): 
1. export FLASK_APP=app
2. python -m flask run
3. Click the link!
"""


import os
from flask import Flask, request, redirect, url_for, render_template
from flask import render_template
from flask import request
import utils_amino_acids_to_chemical_formula


app = Flask(__name__)

# a simple page that serves as the homepage
# @app.route tells Flask the URL that should trigger a call to our function!
@app.route('/')
def home():
    """Landing page of the website."""
    return render_template('home.html')

@app.route('/amino_acids_to_chemical_formula', methods=['GET', 'POST'])
def amino_acids_to_chemical_formula():
    """Input form for converting amino acids to chemical formula."""
    if request.method == 'POST':
        all_form_data: dict[str, str] = dict(request.form)
        sequence_query: str = all_form_data['sequence_query']
        return redirect(url_for('results_amino_acids_to_chemical_formula', sequence_query=sequence_query))
    else:
        return render_template('amino_acids_to_chemical_formula.html')

@app.route('/amino_acids_to_chemical_formula/<sequence_query>')  
def results_amino_acids_to_chemical_formula(sequence_query):
    """Utilize the form data to consult the dictionary and return an appropriate result."""
    result: list[str] = utils_amino_acids_to_chemical_formula.convert_amino_acids_to_formulas(sequence_query)
    return render_template('results_amino_acids_to_chemical_formula.html', result=result)

@app.route('/about')
def about():
    """About page of the website."""
    return render_template('about.html')

if __name__ == "__main__":
	app.run()