# messing with objects
# Author Sharon Curley (lecture)

class Nameofclass:
    name = ""
    last = ""
    def getfullname(self):
        return self.name + " " + self.last

inst = Nameofclass()
inst2 = Nameofclass()

inst.name = "Sharon"
inst2.last = "Curley"

person = inst
print (person.name)

inst.last = "bloks"
print (person.getfullname())

str1 = "blah"
str2 = str1

str1 += "with bells"

print (str2)
