

from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     print (processed_text)
#     return processed_text

# @app.route('/', methods=['POST'])
# def submit_textarea():
#     # store the given text in a variable
#     text = request.form.get("text")
#     print(text)

@app.route('/submit', methods=['POST'])
def submit():
    return 'You entered: {}'.format(request.form['text'])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3002))
    app.run(host = '0.0.0.0', port = port, debug = True)





