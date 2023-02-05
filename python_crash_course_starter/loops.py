# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people_ke = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person_ke in people_ke:
  print(f'Current Person: {person_ke}')

# Break
for person_ke in people_ke:
  if person_ke == 'Sara':
    break
  print(f'Current Person: {person_ke}')

# Continue
for person_ke in people_ke:
  if person_ke == 'Sara':
    continue
  print(f'Current Person: {person_ke}')

# range
for i_ke in range(len(people_ke)):
  print(people_ke[i_ke])

for i_ke in range(0, 11):
  print(f'Number: {i_ke}')

# While loops execute a set of statements as long as a condition is true.

count_ke = 0
while count_ke < 10:
  print(f'Count: {count_ke}')
  count_ke += 1