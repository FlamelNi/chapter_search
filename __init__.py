

from flask import Flask, request, render_template
import os
from pyt import breakToWords
from pyt import getImportantKeys

app = Flask(__name__)

def getKeyWords():
    # currently, this returns dummy data
    # return [ ["worda", 1, 1],
    #     ["wordb", 3, 2],
    #     ["wordc", 2, 2],
    #     ["wordd", 2, 1] ]
    return getImportantKeys()
    
    

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    a = [format(request.form['text'])]
    
    listOfWords = breakToWords(a)
    
    keyWords = getKeyWords()
    selectedWords = []
    
    for word in listOfWords:
        for keyWord in keyWords:
            if word == keyWord[0]:
                selectedWords.append([word, keyWord[2]])
    
    
    countedSelectedWords = []
    exists = 0
    for chosen in selectedWords:
        exists = 0
        for alreadyCounted in countedSelectedWords:
            if chosen[0] == alreadyCounted[0]:
                alreadyCounted[2] = alreadyCounted[2] + 1
                exists = 1
        if exists == 0:
            countedSelectedWords.append([ chosen[0], chosen[1], 1 ])
    
    #test print
    # for alreadyCounted in countedSelectedWords:
    #     print(alreadyCounted[0] + " " + str(alreadyCounted[1]) + " " + str(alreadyCounted[2]) )
    
    # hello my name is Jay. worda is awesome and wordc too. wordb is the best but I like worda better
    
    return 'Done'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3002))
    app.run(host = '0.0.0.0', port = port, debug = True)





