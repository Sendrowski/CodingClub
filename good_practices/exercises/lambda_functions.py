import numpy as np

# dict of people
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 35},
    {'name': 'Daisy', 'age': 28}
]

# get names of people under 30
names = [person['name'] for person in people if person['age'] < 30]

# TODO: Reimplement the above using a lambda function
young_people = list(filter(lambda person: person, people))
names2 = list(map(lambda person: person, young_people))

# check that the results are the same
np.testing.assert_array_equal(names, names2)

print("Exercise completed successfully!")
