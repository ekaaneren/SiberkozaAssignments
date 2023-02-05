# If/ Else conditions are used to decide to do something based on something being true or false

x_ke = 21
y_ke = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x_ke > y_ke:
  print(f'{x_ke} is greater than {y_ke}')

# If/else
if x_ke > y_ke:
  print(f'{x_ke} is greater than {y_ke}')
else:
  print(f'{y_ke} is greater than {x_ke}')  

# elif
if x_ke > y_ke:
  print(f'{x_ke} is greater than {y_ke}')
elif x_ke == y_ke:
  print(f'{x_ke} is equal to {y_ke}')  
else:
  print(f'{y_ke} is greater than {x_ke}')  

# Nested if
if x_ke > 2:
  if x_ke <= 10:
    print(f'{x_ke} is greater than 2 and less than or equal to 10')
    

# Logical operators (and, or, not) - Used to combine conditional statements

# and
if x_ke > 2 and x_ke <= 10:
    print(f'{x_ke} is greater than 2 and less than or equal to 10')

# or
if x_ke > 2 or x_ke <= 10:
    print(f'{x_ke} is greater than 2 or less than or equal to 10')

# not
if not(x_ke == y_ke):
  print(f'{x_ke} is not equal to {y_ke}')


# Membership Operators (not, not in) - Membership operators are used to test if a sequence is presented in an object

numbers = [1,2,3,4,5]

#  in
if x_ke in numbers:
  print(x_ke in numbers)

# not in
if x_ke not in numbers:
  print(x_ke not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# is
if x_ke is y_ke:
  print(x_ke is y_ke)

# is not
if x_ke is not y_ke:
  print(x_ke is not y_ke)
