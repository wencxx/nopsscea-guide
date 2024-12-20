from flask import Flask, render_template
from blueprints.main import main

app = Flask(__name__, template_folder='templates')


app.register_blueprint(main, url_prefix='/')

@app.errorhandler(404)
def index(error):
    return 'Invalid url 404'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3333, debug=True)