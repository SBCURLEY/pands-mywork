# messing with init
# Author: Sharon Curley lecture

class Person:
    def __init__(self, first="", last=""):
        self.firstname = first
        self.lastname = last
        
    def fullName(self):
        if hasattr (self, "middlename"):
            return self.firstname + " " + self.middlename + " " + self.lastname
        return self.firstname+ " "+ self.lastname
        
    def __str__ (self):
        return self.fullName()
    
    def addmiddlename(self, middlename):
        self.middlename = middlename

'''
# Did not work as per lecture

if __name__ == '___main__':                       # can import this module and re-use class somewhere else
    person1 = Person("Sharon",  "Curley")
    print (person1.firstname)
    
    print (person1.fullName())
    person1.addmiddlename("Noreen")

    print (person1)
'''

person1 = Person("Sharon",  "Curley")
print (person1.firstname)
    
print (person1.fullName())
person1.addmiddlename("Noreen")

print (person1)