from flask import Blueprint, jsonify
from web_app.lines.models import Line
from web_app import db

lines = Blueprint('lines', __name__,  template_folder='templates')

@lines.route('/', methods=['GET'])
def get_lines():
    stmt = db.select(Line)
    data = db.session.execute(stmt).all()

    return jsonify([row.Line.serialize for row in data])

@lines.route('/<id>', methods=['GET'])
def get_line_by_id(id):
    data = db.session.get(Line, int(id))
    return jsonify(data.serialize)

@lines.route('/element/<element>', methods=['GET'])
def get_lines_by_element(element):
    stmt = db.select(Line).filter(Line.element==element)
    data = db.session.execute(stmt).all()

    return jsonify([row.Line.serialize for row in data])