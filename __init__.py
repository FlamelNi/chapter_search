

from flask import Flask, request, render_template
import os
from pyt import breakToWords
from pyt import getImportantKeys
from pyt import breakAndGetKeys

app = Flask(__name__)

# TODO: train with more data
# TODO: link result to html page

def getStats(aList = []):
    # [ [section, percentage]
    #   [section, percentage]
    #   [section, percentage] ]
    return ""
    
    # dummy:
    aList = [  ['a', .3], ['b', .5], ['c', .2]  ]
    
    highSect = ['z', 0]
    sortedList = []
    nextList = []
    
    while len(aList) > 0:
        for sect in aList:
            if sect[1] > highSect[1]:
                if highSect[0] != 'z':
                    nextList.append(highSect)
                highSect = sect
            else:
                nextList.append(sect)
        
        sortedList.append(highSect)
        aList = nextList
        nextList = []
    
    print("out of while")
    
    result = ""
    
    for sect in sortedList:
        result = result + getSectionName(sect[0]) + ": " + str(sect[1]*100) + "%\n"
        
    return result
    
    
    
    
def getSectionLink(name):
    return {
        'a': "https://www.khanacademy.org/science/physics/forces-newtons-laws",
        'b': "https://www.khanacademy.org/science/physics/work-and-energy",
        'c': "https://www.khanacademy.org/science/physics/thermodynamics",
        'd': "https://www.khanacademy.org/science/physics/electric-charge-electric-force-and-voltage"
    }.get(name, "https://www.google.com")

def getSectionName(name):
    return {
        'a': "Force/Motion",
        'b': "Energy",
        'c': "Thermodynamics",
        'c': "Electricity"
    }.get(name, "Force/Motion")


def getKeyWords():
    return getImportantKeys()
    
    

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    
    a = [format(request.form['text'])]
    
    countedSelectedWords = breakAndGetKeys(a)
    
    #test print
    for alreadyCounted in countedSelectedWords:
        print(alreadyCounted[0] + " " + str(alreadyCounted[1]) + " " + str(alreadyCounted[2]) )
    
    
    # getSection with machine learning
    section = 'c'
    
    return render_template('element.html', message = getSectionName(section), link = getSectionLink(section), stats=getStats())


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3002))
    app.run(host = '0.0.0.0', port = port, debug = True)





