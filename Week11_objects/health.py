# use person module
# Author :Sharon Curley

from personModule import *

person1 = {
        "firstname":"Sharon",
        "lastname": "Curley",
        "dob": dt.date(2010,1,1),
        "height":100,
        "weight":80
    }
displayperson(person1)
gethealthdata(person1)