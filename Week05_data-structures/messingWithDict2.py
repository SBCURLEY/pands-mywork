# messingWithDict2.py
# more messing with dictionaries
# Here I am looking at for loops
# Author: Sharon Curley (lecture)

car = {
    "make": "Fiat",
    "model" : "Punto",
    "price" : 10000,
    "tags"  : ["pre-owned", "Best Buy", "Dealer"]
}

print("\n")

print (car)

print("\n")

#print out the keys
for key in car:
    print (key)
    print (key, "has value" , car[key])
    
print("\n")
    
for key, value in car.items():
    print(key,"has a value",value)     # comma puts in a space
    
print("\n")