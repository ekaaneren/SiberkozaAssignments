# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person_ke = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Use constructor
# person2_ke = dict(first_name='Sara', last_name='Williams')

# Get value
print(person_ke['first_name'])
print(person_ke.get('last_name'))

# Add key/value
person_ke['phone'] = '555-555-5555'

# Get dict keys
print(person_ke.keys())

# Get dict items
print(person_ke.items())

# Copy dict
person2_ke = person_ke.copy()
person2_ke['city'] = 'Boston'

# Remove item
del(person_ke['age'])
person_ke.pop('phone')

# Clear
person_ke.clear()

# Get length
print(len(person2_ke))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])
