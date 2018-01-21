

def chapterName(x):
    return {
        '1': "1_ForceMotion.txt",
        '2': "2_Energy.txt"
    }.get(x, "1_ForceMotion.txt")    # 9 is default if x not found

def breakToWords(name, LIMIT = 1000000000):
    
    name = chapterName(name)

    with open(name, encoding="utf8") as f:
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


    newContent = []
    newList = []

    a = 0

    while 1:#something wrong here------------------------------------------------
        for line in content:
            if line.find("•") == -1 and not (any(char.isdigit() for char in line) ):
                if line.find(" ") != -1:
                    newList.append( line[:line.find(" ")] )
                    newContent.append( line[line.find(" ")+1:] )
                else:
                    newList.append( line )
            a = a + 1
            if a > LIMIT:
                break
        if len(newContent) == 0:
            break

        content = newContent
        newContent = []
        # print("loop")
    
    
    
    
    newContent = newList
    newList = []
    #removing punctuations
    for x in newContent:
        newList.append(x.replace('.', '').replace(',', '').replace('?', '').replace('(', '').replace(')', '').replace('“', '').replace('\”', '').replace('\"', '').replace('\"', ''))
        
    
    # a = 0
    # newContent = newList;
    # newList = []
    # for line in newContent:
    #     if len(line) > 1:
    #         newList.append( line )
        
    return newList


class wordCount:
    word = ""
    count = 0

def compare(a, b):
    if a.count < b.count:
        return 1
    return 0

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


def getAllCount(name = "1", number = 10000000):
    crudeList = breakToWords(name, number)
    listOfWords = []
    
    exists = 0
    
    for newWord in crudeList:
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
    
    
    
    #sort
    listOfWords = sort(listOfWords)
    
    return listOfWords
    
    


#------------------------main---------------------------


listOfWords = getAllCount("1")

# print
# for wc in listOfWords:
#     print(wc.word + "    " + str(wc.count))


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

