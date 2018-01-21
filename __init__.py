

from flask import Flask, request, render_template
import os
from pyt import breakToWords

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')



def getTextAndFindAllKeyWords(text = ""):
    
    breakToWords()
    
    

@app.route('/submit', methods=['POST'])
def submit():
    
    a = [format(request.form['text'])]
    listOfWords = breakToWords(a)
    for wc in listOfWords:
        print(wc)
    return 'Done'
    # return chapterName("1")
    # return 'You entered: {}'.format(request.form['text'])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3002))
    app.run(host = '0.0.0.0', port = port, debug = True)





