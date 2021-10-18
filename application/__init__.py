"""Running website as package.

To run the website after installing requirements: 
1. export FLASK_APP=draft_product.unc_abbreviations
  - Alternatively, do the following: 
    1) cd draft_product (cd stands for change directory, so this navigates you to the appropriate folder)
    2) export FLASK_APP=unc_abbreviations
2. python -m flask run
3. Click the link!
"""


import os
from flask import Flask
from flask import render_template
from flask import request
from . import constants


def create_app(test_config=None):
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # A local database shouldn't be needed, but just in case...
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that serves as the homepage
    # @app.route tells Flask the URL that should trigger a call to our function!
    @app.route('/', methods=['GET', 'POST'])
    def home():
        """Landing page of the website."""
        return render_template('home.html')
    
    @app.route('/definition', methods=['GET', 'POST'])  
    def definition():
        """Utilize the form data to consult the dictionary and return an appropriate result."""
        # Get inputted data.
        # TODO: what is the original type of request.form['search_query']?
        result: str = constants.NO_RESULT_FOUND
        search_query = str(request.form['search_query'])
        if search_query in constants.WORD_BANK:
            result = constants.WORD_BANK[search_query]
        return render_template('definition.html',result=result)

    return app