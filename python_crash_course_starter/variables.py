# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name_ke and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# x_ke = 1           # int
# y_ke = 2.5         # float
# name_ke = 'John'   # str
# is_cool_ke = True  # bool

# Multiple assignment
x_ke, y_ke, name_ke, is_cool_ke = (1, 2.5, 'John', True)

# Basic math
a = x_ke + y_ke

# Casting
x_ke = str(x_ke)
y_ke = int(y_ke)
z = float(y_ke)

print(type(z), z)