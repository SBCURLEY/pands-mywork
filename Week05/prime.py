# prime.py
# generate primes
# Author: Sharon Curley (lecture)

primes = []
upto = 100

for candidate in range(2,upto):        
    # put in variables instead of hard coding a number
    isPrime = True
    #only need to check if divisable by prime
    for divisor in primes:
    #if divisable by an int, it is not a Prime Number
        if(candidate% divisor ==0):
            isPrime=False
            #so there is no reason to keep checking
            break
        
    if isPrime:
        primes.append(candidate)

print (primes)