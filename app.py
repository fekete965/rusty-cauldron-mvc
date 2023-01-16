import os

from flask import Flask

from constants import RUSTY_CAULDRON_KEY

App = Flask(__name__)

if not os.environ[RUSTY_CAULDRON_KEY]:
	raise Exception(f"{RUSTY_CAULDRON_KEY} must be defined in your environment!")
    
App.secret_key = os.environ[RUSTY_CAULDRON_KEY]

import routes
