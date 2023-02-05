# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

#  Sample JSON
userJSON_ke = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse to dict
user_ke = json.loads(userJSON_ke)

# print(user_ke)
# print(user_ke['first_name'])

car_ke = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJSON_ke = json.dumps(car_ke)

print(carJSON_ke)
