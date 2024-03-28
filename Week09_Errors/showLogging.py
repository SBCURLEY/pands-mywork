# showLogging.py
# Demonstrate logging
# Attributes you can put in the basicConfig
#   level  DEBUG INFO WARNING ERROR
#   filename
#   filemode
#   format
#       %(name)s - %(levelname)s - %(message)s -  %(asctime)s - %(lineno)d

import logging

'''
logging.basicConfig(level=logging.DEBUG)
# program does stuff
logging.debug ("we are doing stuff")               # Result = DEBUG:root:we are doing stuff
'''

'''
logging.basicConfig(level=logging.WARNING)           # DEBUG shows all messages, changing to WARNING only shows warning, error & critical.
# program does stuff
logging.debug ("we are doing stuff")               # Result = DEBUG:root:we are doing stuff
logging.info("This is information")
logging.warning("I am not certain about this")
logging.error("Not good")
logging.critical("Really bad")
'''


logging.basicConfig(filename="./mainlog.log",
                    level=logging.DEBUG,              # DEBUG shows all messages, changing to WARNING only shows warning, error & critical.
                    format="(%(asctime)s-%(levelname)s-%(message)s-%(lineno)d")           

# program does stuff
logging.debug ("we are doing stuff")               # Result = DEBUG:root:we are doing stuff
logging.info("This is information")
logging.warning("I am not certain about this")
logging.error("Not good")
logging.critical("Really bad")


