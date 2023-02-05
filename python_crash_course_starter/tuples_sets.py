# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits_ke = ('Apples', 'Oranges', 'Grapes')

# Using a constructor
# fruits2_ke = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2_ke = ('Apples',)

# Get value
print(fruits_ke[1])

# Can't change value
fruits_ke[0] = 'Pears'

# Delete tuple
del fruits2_ke

# Get length
print(len(fruits_ke))

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set_ke = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set_ke)

# Add to set
fruits_set_ke.add('Grape')

# Remove from set
fruits_set_ke.remove('Grape')

# Add duplicate
fruits_set_ke.add('Apples')

# Clear set
fruits_set_ke.clear()

# Delete
del fruits_set_ke

print(fruits_set_ke)
