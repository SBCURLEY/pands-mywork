# lab05.01-quiz.py
# Quiz
# Author: Sharon Curley

numberOfQuestions = 5
averageAge = 23.4
debugMode = True
name = "Joe"
ages = []
months = ("Jan", "Feb", "Mar")
book = {}
stuff = [12,"Fred", False, {}]
someone = dict(firstname = "Joe")

me = {
    "firstname":"Sharon",
    "teaching": [{
        "courseName":"programming",
        "semester":1
    },{
        "courseName":"Data Representation",
        "semester":2
    }
    ]
}


print(type(numberOfQuestions))       # class 'int'
print(type(averageAge))              # class 'float'
print(type(debugMode))               # boolean  class 'bool'
print(type(name))                    # string  class 'str'
print(type(ages))                    # list  class 'list'
print(type(months))                  # class 'tuple'
print(type(months[1]))               # string  class 'str'
print(type(book))                    # dict   class 'dict'
print(type(stuff))                   # tuple  class 'tuple'  ???????????????
print(type(stuff[2]))                # boolean  class 'bool'
print(type(someone))                 # dict
print(type(someone["firstname"]))    # string
print(type(me))                      # dict
print(type(me["teaching"]))          # list
print(type(me["teaching"][0]["semester"]))    # dict  NO      class 'int'
print(type(me["teaching"][0]["courseName"]))   ## Changed the n  to N: dict  NO    class 'str'
