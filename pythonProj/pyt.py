

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
        a = a + 1
        if a > LIMIT:
            break
        
        # print("loop")
    
    #removing punctuations
    a = 0
    newContent = newList;
    newList = []
    for line in newContent:
        if line.find(".") != -1:
            newList.append( line[:line.find(".")] )
        elif line.find(",") != -1:
            newList.append( line[:line.find(",")] )
        elif line.find("?") != -1:
            newList.append( line[:line.find("?")] )
        else:
            newList.append( line )
        
    # a = 0
    # newContent = newList;
    # newList = []
    # for line in newContent:
    #     if len(line) > 1:
    #         newList.append( line )
        
    return newList



#------------------------main---------------------------

a = breakToWords("", 300)
print(a)




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

