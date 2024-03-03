# lab06.05-readModules.py
# We can now think about how to read in the modules. 
# We want to keep reading modules until the user enters a module name of blank.

def readModules ():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module ["name"] = moduleName
        # There is no error handling
        module["grade"]=int(input("\t\tEnter grade: "))
        modules.append(module)
        # Now read the next module
        moduleName = input("\tEnter the next Module name (blank to quit) :").strip()
        
    return modules

