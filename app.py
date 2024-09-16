from flask import Flask, render_template, request, flash, redirect, url_for
from models import User
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/result')
def result():
	ret_val = request.args.get('id')

	return render_template("results.html", ret_val=ret_val)

if __name__ == '__main__':
    app.run(debug=)

