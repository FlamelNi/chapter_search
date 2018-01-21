

from flask import Flask, request, render_template
import os
# import 

os.chdir("../pythonProj/pyt.py")

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')



def getTextAndFindAllKeyWords(text = ""):
    
    breakToWords()
    
    




@app.route('/submit', methods=['POST'])
def submit():
    
    
    return 'You entered: {}'.format(request.form['text'])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3002))
    app.run(host = '0.0.0.0', port = port, debug = True)





