"""
	doc:	https://docs.python.org/3/howto/logging.html
"""

import logging

# Create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# Ceate console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formater
formater = logging.Formater('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formater to ch
ch.setFormater(formater)

# Add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

""" output:

	$ python simple_logging_module.py
		2005-03-19 15:10:26,618 - simple_example - DEBUG - debug message
		2005-03-19 15:10:26,620 - simple_example - INFO - info message
		2005-03-19 15:10:26,695 - simple_example - WARNING - warn message
		2005-03-19 15:10:26,697 - simple_example - ERROR - error message
		2005-03-19 15:10:26,773 - simple_example - CRITICAL - critical message
"""