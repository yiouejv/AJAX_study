from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return 'index'


@app.route('/xmlhttprequest/')
def xmlhttprequest():
    return render_template('XMLHttpRequest.html')


if __name__ == '__main__':
    app.run()
