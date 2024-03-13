# lab07.01-quiz-a.py
# the with statement will automatically close the file
# when it is finished with it

with open("test-a.txt") as f:
    data = f.read()
    print (data)
    
# The old way
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()


# a) nothing as no file exists. There is an error