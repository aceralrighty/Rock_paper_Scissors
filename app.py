from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/result')
def result():
    ret_val = request.args.get('id')

    if not ret_val:
        ret_val = 'No ID provided'

    return render_template("results.html", ret_val=ret_val)

def total_wins():
    ret_score = request.args.get('score')

if __name__ == '__main__':
    app.run(debug=True)
