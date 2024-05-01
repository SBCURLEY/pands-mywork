# demo of a module
#
# Author: Sharon Curley

import datetime as dt 

def gethealthdata(person):
    print("get health data: ", person["firstname"])
    
def displayperson(person):
    print(person)
    
if __name__ == '__main__':
    person1 = {
        "firstname":"Sharon",
        "lastname": "Curley",
        "dob": dt.date(2010,1,1),
        "height":100,
        "weight":80
    }
    
displayperson(person1)
gethealthdata(person1)