

from flask import Flask, request, render_template
import os
from pyt import breakToWords
from pyt import getImportantKeys

app = Flask(__name__)

def getSectionLink(name):
    return {
        'a': "https://www.khanacademy.org/science/physics/forces-newtons-laws",
        'b': "https://www.khanacademy.org/science/physics/work-and-energy",
        'c': "https://www.khanacademy.org/science/physics/thermodynamics"
    }.get(name, "https://www.google.com")

def getSectionName(name):
    return {
        'a': "Force/Motion",
        'b': "Energy",
        'c': "Thermodynamics"
    }.get(name, "Force/Motion")


def getKeyWords():
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
    for alreadyCounted in countedSelectedWords:
        print(alreadyCounted[0] + " " + str(alreadyCounted[1]) + " " + str(alreadyCounted[2]) )
    
    
    # getSection with machine learning
    section = 'b'
    
    return render_template('element.html', message = getSectionName(section), link = getSectionLink(section))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3002))
    app.run(host = '0.0.0.0', port = port, debug = True)





