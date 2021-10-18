"""Running website as package.

To run the website from source code after installing requirements (may need to rename main to be __init__.py): 
1. export FLASK_APP=app
2. python -m flask run
3. Click the link!
"""


import os
import re
from flask import Flask, request, redirect, url_for, render_template
from flask import render_template
from flask import request
import utils_amino_acids_to_chemical_formula
import constants
import time


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.config.from_mapping(
    TEMP_FOLDER=constants.RESULT_CSV_FOLDER_PATH
)

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
        sequence_query: str = validate_input(all_form_data['sequence_query'])
        return redirect(url_for('results_amino_acids_to_chemical_formula', sequence_query=sequence_query))
    else:
        return render_template('amino_acids_to_chemical_formula.html')

@app.route('/amino_acids_to_chemical_formula/<sequence_query>')  
def results_amino_acids_to_chemical_formula(sequence_query):
    """Utilize the form data to consult the dictionary and return an appropriate result."""
    list_sequences: list[str] = utils_amino_acids_to_chemical_formula.read_in_sequences(sequence_query)
    result: dict[str, str] = utils_amino_acids_to_chemical_formula.sequences_to_formulas_dict(list_sequences)

    # past_csvs = list(os.listdir(os.path.join(os.getcwd(), constants.RESULT_CSV_FOLDER_PATH)))
    # past_csvs_times = [filename_to_time(filename) for filename in past_csvs]

    # # Partially based on https://linuxize.com/post/python-delete-files-and-directories/
    # csv_deletion_threshold: float = time.time() - (constants.LENGTH_DAY * constants.LIMIT_DAYS)
    # i: int = 0
    # while i < len(past_csvs):
    #     file_path = os.path.join(constants.RESULT_CSV_FOLDER_PATH, past_csvs[i])
    #     if float(past_csvs_times[i]) < csv_deletion_threshold:
    #         try:
    #             os.remove(file_path)
    #         except OSError as e:
    #             print("Error: %s : %s" % (file_path, e.strerror))
    #     i += 1

    csv_path: str = utils_amino_acids_to_chemical_formula.generate_result_csv(list_sequences)

    return render_template('results_amino_acids_to_chemical_formula.html', result=result, csv_path=csv_path)

@app.route('/about')
def about():
    """About page of the website."""
    return render_template('about.html')

def filename_to_time(filename: str) -> str:
    """Get time of creation of a csv from its file name."""
    trim_prefix: str = re.sub(constants.RESULT_CSV_NAME_BEGINNING, "", filename)
    trim_end: str = re.sub(constants.RESULT_CSV_PATH_EXTENSION, "", trim_prefix)
    return trim_end

def validate_input(input_str) -> str:
    validated_input: str = ""
    for character in input_str:
        if character == constants.NEW_LINE:
            validated_input += character
        elif (character.upper() in constants.VALID_AMINO_ACIDS):
            validated_input += character.upper()
    
    return validated_input

if __name__ == "__main__":
	app.run()