# myFunctions.py
## a module of useful functions
# Author: Sharon Curley (lecture notes)

import logging
logging.basicConfig(filename="./bank.log",
                    level=logging.DEBUG,
                    format="%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(lineno)d")

balance = 100

def withdraw(amount):
    global balance
    if amount < 0:
        logging.critical(f"the amount ({amount}) should never be less than 0")
        raise ValueError("amount should always be greater than 0")
    if amount > balance:
        logging.warning(f"trying to withdraw more ({amount}) than is in account ({balance})")
        raise ValueError("not enough funds")
    balance = balance - amount
    logging.info(f"we have just withdrawn {amount} new balance is{balance}")
    return balance

if __name__ == "__main__":                                      # this will ony run when myfunctions.py is run. Not in a test program
    assert withdraw(110) == 80 , "incorrect calculation"         # if the calculation is correct(20), print all good. If not (10), it will give an assert error incorrect calculation
    try:
        withdraw(-1)
        assert False, "should have thrown a value error"        # try -1 - AssertionError:should have thrown a value error
    except ValueError as ve:                                    
        pass
    
    try:
        withdraw(110)                                           # withdrawing more than what is in there
        assert False, "can't withdraw more than is in balance"
    except ValueError as ve:
        pass
    print ("all good")