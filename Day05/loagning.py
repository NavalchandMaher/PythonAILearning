

#Basic Logging
import logging

#logging.basicConfig(level=logging.INFO)
#logging.basicConfig(filename="app.log", level=logging.INFO)
#Better Logging Format
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


#Singleton Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")

#Logging Levels

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

#Singleton Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('app.log')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.info("This is an info message from the singleton logger")
logger.warning("This is a warning message from the singleton logger")
logger.error("This is an error message from the singleton logger")
logger.critical("This is a critical message from the singleton logger")