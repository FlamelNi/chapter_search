

totalsInEachSection = {}


def getQuestion(number):
    return {
        0: "A potential difference of 1.20 V will be applied to a 33.0 m length of 18-gauge copper wire (diameter ! 0.0400 in.). Calculate (a) the current, (b) the magnitude of the current density, (c) the magnitude of the electric field within the wire, and (d) the rate at which thermal energy will appear in the wire.",
        1: "(a) What is the electric potential energy of two electrons separated by 2.00 nm? (b) If the separation increases, does the potential energy increase or decrease?",
        2: "Suppose that you intercept 5.0 ' 10$3 of the energy radiated by a hot sphere that has a radius of 0.020 m, an emissivity of 0.80, and a surface temperature of 500 K. How much energy do you intercept in 2.0 min?",
        3: "An object of mass 6.00 kg falls through a height of 50.0 m and, by means of a mechanical linkage, rotates a paddle wheel that stirs 0.600 kg of water. Assume that the initial gravitational potential energy of the object is fully transferred to thermal energy of the water, which is initially at 15.0 C. What is the temperature rise of the water?",
        4: "A horizontal force of magnitude 35.0 N pushes a block of mass 4.00 kg across a floor where the coefficient of kinetic friction is 0.600. (a) How much work is done by that applied force on the block–floor system when the block slides through a displacement of 3.00 m across the floor? (b) During that displacement, the thermal energy of the block increases by 40.0 J.What is the increase in thermal energy of the floor? (c) What is the increase in the kinetic energy of the block?",
        5: "A large fake cookie sliding on a horizontal surface is attached to one end of a horizontal spring with spring constant k ! 400 N/m; the other end of the spring is fixed in place. The cookie has a kinetic energy of 20.0 J as it passes through the spring’s equilibrium position. As the cookie slides, a frictional force of magnitude 10.0 N acts on it. (a) How far will the cookie slide from the equilibrium position before coming momentarily to rest? (b) What will be the kinetic energy of the cookie as it slides back through the equilibrium position?",
        6: "The floor of a railroad flatcar is loaded with loose crates having a coefficient of static friction of 0.25 with the floor. If the train is initially moving at a speed of 48 km/h, in how short a distance can the train be stopped at constant acceleration without causing the crates to slide over the floor?",
        7: "The velocity of a 3.00 kg particle is given by  (8.00t + 3.00t2 ) m/s, with time t in seconds. At the instant the net force on the particle has a magnitude of 35.0 N, what are the direction (relative to the positive direction of the x axis) of (a) the net force and (b) the particle’s direction of travel?",
        8: "Using a rope that will snap if the tension in it exceeds 387 N, you need to lower a bundle of old roofing material weighing 449 N from a point 6.1 m above the ground. Obviously if you hang the bundle on the rope, it will snap. So, you allow the bundle to accelerate downward. (a)What magnitude of the bundle’s acceleration will put the rope on the verge of snapping? (b) At that acceleration, with what speed would the bundle hit the ground?",
        9: "Figure 7-23 shows three arrangements of a block attached to identical springs that are in their relaxed state when the block is centered as shown. Rank the arrangements according to the magnitude of the net force on the block, largest first, when the block is displaced by distance d (a) to the right and (b) to the left. Rank the arrangements according to the work done on the block by the spring forces, greatest first, when the block is displaced by d (c) to the right and (d) to the left.",
        10: "(a) What is the rate of energy loss in watts per square meter through a glass window 3.0 mm thick if the outside temperature is $20 F and the inside temperature is 72 F? (b) A storm window having the same thickness of glass is installed parallel to the first window, with an air gap of 7.5 cm between the two windows. What now is the rate of energy loss if conduction is the only important energy-loss mechanism?",
        11: "Figure 21-30a shows an arrangement of three charged particles separated by distance d. Particles A and C are fixed on the x axis, but particle B can be moved along a circle centered on particle A. During the movement, a radial line between A and B makes an angle u relative to the positive direction of the x axis (Fig. 21-30b). The curves in Fig. 21-30c give, for two situations, the magnitude Fnet of the net electrostatic force on particle A due to the other particles.That net force is given as a function of angle u and as a multiple of a basic amount F0. For example on curve 1, at u # 180-, we see that Fnet # 2F0. (a) For the situation corresponding to curve 1, what is the ratio of the charge of particle C to that of particle B (including sign)? (b) For the situation corresponding to curve 2, what is that ratio?"
        
    }.get(number, "")


#Gets name of textfile that contains physics info, separated by sections
#parameter 'x' has to be string-ed number such as "1", not 1
def chapterName(x):
    return {
        '1': "a_ForceMotion.txt",
        '2': "b_Energy.txt",
        '3': "c_Thermo.txt",
        '4': "d_Electro.txt"
    }.get(x, "a_ForceMotion.txt")    # default if x not found


#gets list of string as parameter and returns the same but all strings in lowercase
def lowerStringList(stringList):
    newList = []
    for single in stringList:
        newList.append(single.lower())
    return newList


# Parameter "content" is list that contains multiple sentences.
# This function will break content into multiple parts and build one list of words
def breakToWords(content = []):
    
    content = lowerStringList(content)

    newContent = []
    newList = []

    while 1:
        for line in content:
            if line.find("•") == -1:
                if line.find(" ") != -1:
                    newList.append( line[:line.find(" ")] )
                    newContent.append( line[line.find(" ")+1:] )
                else:
                    newList.append( line )
        if len(newContent) == 0:
            break
        content = newContent
        newContent = []
    
    
    newContent = newList
    newList = []
    
    
    for word in newContent:
        if not any(char.isdigit() for char in word):
            newList.append(word)
    
    newContent = newList
    newList = []
    #removing punctuations
    for x in newContent:
        newList.append(x.replace('.', '').replace(',', '').replace('?', '').replace('(', '').replace(')', '').replace('“', '').replace('\”', '').replace('\"', '').replace('\"', '').replace('!', ''))
        
    newContent = newList
    newList = []
    
    for x in newContent:
        if len(x) > 0:
            newList.append(x)
    
    
    
    
    # a = 0
    # newContent = newList;
    # newList = []
    # for line in newContent:
    #     if len(line) > 1:
    #         newList.append( line )
    
    return newList

# reads from textfile and break it by handing it in to break to words
def getFromFile(i):
    
    i = chapterName(i)

    with open(i, encoding="utf8") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    
    for line in content:
        if line == "":
            content.remove("")
        if line == " ":
            content.remove(" ")

    while "" in content or " " in content:
        if "" in content:
            content.remove("")
        if " " in content:
            content.remove(" ")
        if "\"" in content:
            content.remove("\"")
    
    return breakToWords(content)

# class declaration of wordCount
class wordCount:
    word = ""
    count = 0

# this just compares two wordCount object
def compare(a, b):
    if a.count < b.count:
        return 1
    return 0

# this sorts a list of wordCount objects and returns sorted list (by count)
def sort(unsorted):
    a = 0
    begin = 0

    while begin < len(unsorted):
        best = begin
        a = begin + 1
        while a < len(unsorted):
            if compare(unsorted[a], unsorted[best]):
                best = a
            a = a + 1

        temp = unsorted[begin]
        unsorted[begin] = unsorted[best]
        unsorted[best] = temp

        begin = begin + 1

    return unsorted

# gets sorted list of wordCount objects from textfiles
def getAllCount(i = "1"):
    crudeList = getFromFile(i)
    listOfWords = []
    
    exists = 0
    
    totalCount = 0
    
    for newWord in crudeList:
        totalCount = totalCount + 1
        for wc in listOfWords:
            exists = 0
            if wc.word == newWord:
                wc.count = wc.count + 1
                exists = 1
                break
        if exists == 0:
            newWc = wordCount()
            newWc.word = newWord
            newWc.count = 1
            listOfWords.append(newWc)
    
    totalsInEachSection[i] = totalCount
    
    #sort
    listOfWords = sort(listOfWords)
    return listOfWords
    
    
# this function will use getAllCount but re-format it to better-list
# (this does not involve with class/objects)
def finalData():
    
    crudeList = [ getAllCount("1"),
                  getAllCount("2"),
                  getAllCount("3"),
                  getAllCount("4") ]
    
    finalList = []
    
    count = 0
    
    for singleList in crudeList:
        count = count + 1
        for wc in singleList:
            finalElement = [wc.word, wc.count, count]
            finalList.append(finalElement)
    
    return finalList
    

def checkCloseEnough(a, b):
    ALPHA_VALUE = 30
    if abs(a-b)/((a+b)/2)*100 < ALPHA_VALUE:
        return 1
    return 0

def getImportantKeys():
    IMPORTANCE_POINT = 30
    
    allKeys = finalData()
    newKeys = []
    
    exists = 0
    
    for key in allKeys:
        exists = 0
        for newKey in newKeys:
            shouldBreak = 0
            if key[0] == newKey[0]:
                exists = 1
                if checkCloseEnough(key[1], newKey[1]) == 1:
                    shouldBreak = 1
                    newKey[3] = newKey[3] + 1
                elif key[1] > newKey[1]:
                    shouldBreak = 1
                    newKeys.remove(newKey)
                    newKeys.append([key[0],key[1],key[2],0])
            if shouldBreak == 1:
                break
        if exists == 0:
            #name, importance, sections
            newKeys.append([key[0],key[1],key[2],0])
    
    
    allKeys = newKeys
    newKeys = []
    
    for key in allKeys:
        if key[1] >= IMPORTANCE_POINT:
            newKeys.append(key)
    
    allKeys = newKeys
    newKeys = []
    
    for key in allKeys:
        if key[3] < 3:
            newKeys.append([key[0],key[1],key[2]])
    
    
    return newKeys
    
    
def breakAndGetKeys(a):
    listOfWords = breakToWords(a)
    keyWords = getImportantKeys()
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
            
    return countedSelectedWords

#-----------------------------------------------------------
#Y-List

def make_y_list():

    sample_quiz_solution = {"Section": ['D','D','C','C','B','B','A','A']}
    df = pd.DataFrame(sample_quiz_solution)
    dummies = pd.get_dummies(df)
    answer_list = dummies.values.tolist()

    return answer_list

#----------------------------------------------------------
#X-List

    
    
def make_x_list():
    
    listZ = []
    qList = [0,0,0,0]
    
    i = 0
    while i < 8:
        qList = [0,0,0,0]
        aString = getQuestion(i)
        keys = breakAndGetKeys([aString])
        for key in keys:
            qList[ key[1]-1 ] = qList[ key[1]-1 ] + key[2]
        
        listZ.append(qList)
        i = i + 1
    
    return listZ
    
def get_x_list():
    return [[0, 2, 2, 39], [0, 3, 0, 14], [0, 6, 3, 17], [3, 5, 6, 28], [11, 18, 3, 39], [5, 15, 4, 41], [8, 1, 0, 26], [4, 1, 0, 40]]
    
    
def make_z_list():
    
    listZ = []
    qList = [0,0,0,0]
    
    i = 8
    while i < 12:
        qList = [0,0,0,0]
        aString = getQuestion(i)
        keys = breakAndGetKeys([aString])
        for key in keys:
            qList[ key[1]-1 ] = qList[ key[1]-1 ] + key[2]
        
        listZ.append(qList)
        i = i + 1
    
    return listZ
    
def get_z_list():
    return [[5, 3, 0, 32], [1, 15, 2, 44], [2, 2, 2, 40], [4, 1, 10, 94]]
    
    
    
#------------------------main---------------------------

# print(breakAndGetKeys([getQuestion(0)]))
# 
qList = make_z_list()
print(qList)
# 
# for a in qList:
#     print(a[0] + " " + a[1] + " " + a[2] + " " + a[3])


# breakAndGetKeys(getQuestion(0))



# lista = getImportantKeys()
# for key in lista:
#     print(key[0] + " " + str(key[1]) + " " + str(key[2]))


#--------------------help commands-----------------------


# sum = 0
# for i in range(1,11):
#   print(i)
#   sum = sum + i
# print(sum)


# import 
# numpy # array and matrix
# scipy
# pandas
# matplotlib




# array with changeable size
# class
# fstream



# x = input("Enter x: ")
# type()
# int(x)
# print("x is " + x)



# '''
# description is here
# '''



# a = [1, "hello"]

# a[1] = "test"

# def fib(number):
#   '''
#   function description is here
#   '''
#   if number > 2:
#     return fib(number-1) + fib(number-2)
#   return 1

# a = 1

# while a <= 10:
#   print(fib(a))
#   a = a + 1


# x = 0
# while x<4 :
#   print(x)
#   x = x + 1

# for(int i = 0; i < size; i++)
# {}

# for a in [1,2,4,5]:
#   print a

# x = 5

# if x == 5:
#   print("x is 5")



# print("hello world")

# x = 12

# y = "Hi"

# print(str(x) + y)

# def functionName(u):
#   return u+2

# print(functionName(3))

