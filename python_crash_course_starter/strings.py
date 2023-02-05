# Strings in python are surrounded by either single or double quotation marks. Let's_ke look at string formatting and some string methods

name_ke = 'Brad'
age_ke = 37

# Concatenate
print('Hello, my name_ke is ' + name_ke + ' and I am ' + str(age_ke))

# String Formatting

# Arguments by position
print('My name_ke is {name_ke} and I am {age_ke}'.format(name_ke=name_ke, age_ke=age_ke))

# F-Strings (3.6+)
print(f'Hello, my name_ke is {name_ke} and I am {age_ke}')

# String Methods

s_ke = 'helloworld'

# Capitalize string
print(s_ke.capitalize())

# Make all uppercase
print(s_ke.upper())

# Make all lower
print(s_ke.lower())

# Swap case
print(s_ke.swapcase())

# Get length
print(len(s_ke))

# Replace
print(s_ke.replace('world', 'everyone'))

# Count
sub_ke = 'h'
print(s_ke.count(sub_ke))

# Starts with
print(s_ke.startswith('hello'))

# Ends with
print(s_ke.endswith('d'))

# Split into a list
print(s_ke.split())

# Find position
print(s_ke.find('r'))

# Is all alphanumeric
print(s_ke.isalnum())

# Is all alphabetic
print(s_ke.isalpha())

# Is all numeric
print(s_ke.isnumeric())