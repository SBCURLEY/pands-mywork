# messingWithDict1a.py
# Messing with dictionaries
# Author: Sharon Curley (lecture)


#make = "Hyundai"
#model = "Kona"
#Year = "2022"
#Owner = "Sharon"

# want to store two bits of information in the same dict - Owner and Driver No
# Dict object in a dict object

Car={
    "Make" : "Hyundai",
    "Model" : "Kona",
    "Year" : "2022",
    "Owner":{                                                             # Owner is a dict object inside car
         "Name" : "Sharon",
          "Driver-number" : "12345"
    }
}

print (Car["Make"])
attr = "Year"                                                             # make the variable you want to print out an attribute
print(Car[attr])
print (Car)
print (Car["Owner"])                            # prints the dict object     {'Name': 'Sharon', 'Driver-number': '12345'}
print (Car["Owner"]["Name"])                   # want the owners name in that dict
print (Car["Owner"]["Driver-number"])         # want the driver number in that dict
print (type(Car["Owner"].get("Driver-number")))       # get is a handy way if getting a key to tell you is it exists or not. ans= <class 'str'>
print (type(Car["Owner"].get("Driver-no")))           # ans = <class 'NoneType'>   as "Driver-No" does not exist