from flask import Blueprint
from web_app.lines.models import Line

lines = Blueprint('lines', __name__,  template_folder='templates')

@lines.route('/', methods=['GET'])
def get_lines():
    return {
        'line':{
            'wavelength': 532,
            'g': 4,
            'A': 5000
        }
    }