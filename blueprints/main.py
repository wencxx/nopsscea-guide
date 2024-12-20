import json
import os
from flask import Blueprint, render_template, jsonify, url_for, current_app

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/')
def index():
    json_path = os.path.join(current_app.root_path, 'static', 'data', 'objectives.json')
    
    with open(json_path, 'r') as file:
        data = json.load(file)

    return render_template('index.html', objectives=data)

@main.route('/documents')
def documents():
    return render_template('documents.html')

@main.route('/about-us')
def about():
    json_path = os.path.join(current_app.root_path, 'static', 'data', 'members.json')
    
    with open(json_path, 'r') as file:
        data = json.load(file)

    return render_template('about.html', members=data)