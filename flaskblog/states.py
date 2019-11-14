import json


with open('./flaskblog/states.json', 'r') as f:
    states_data = json.load(f)


print(states_data['states'])
