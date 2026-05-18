## convert JSON from python
import json
person = {"name":"john", "age": 30 , "city": "london", "havechildrens":False, "titles":["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
"""print(personJSON)"""

# to create an json file

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)


# covert python from JSON

person = json.loads(personJSON)
print(person)