# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time

# Pip module
from camelcase import CamelCase

# Import custom module
import validator
from validator import validate_email_ke

# today_ke = datetime.date.today_ke()
today_ke = date.today()
timestamp_ke = time()

c_ke = CamelCase()
# print(c_ke.hump('hello there world'))

email_ke = 'test#test.com'
if validate_email_ke(email_ke):
  print('Email is valid')
else:
  print('Email is bad')