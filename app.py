from flask import Flask
from ajax import ajax_bp
from json_ import json_bp

app = Flask(__name__)

app.register_blueprint(ajax_bp)
app.register_blueprint(json_bp)


if __name__ == '__main__':
    app.run(debug=True)
