# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers_ke = [1, 2, 3, 4, 5]
fruits_ke = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1, 2, 3, 4, 5))

# Get a value
print(fruits_ke[1])

# Get the last value
print(fruits_ke[-1])



# Get length
print(len(fruits_ke))

# Append to list
fruits_ke.append('Mangos')

# Remove from list
fruits_ke.remove('Grapes')

# Insert into position
fruits_ke.insert(2, 'Strawberries')

# Change value
fruits_ke[0] = 'Blueberries'

# Remove with pop
fruits_ke.pop(2)

# Reverse list
fruits_ke.reverse()

# Sort list
fruits_ke.sort()

# Reverse sort
fruits_ke.sort(reverse=True)

print(fruits_ke)


