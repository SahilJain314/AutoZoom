import json

#An example class is given. 'time' is input in 24 hour format, no colon
#'prompt' will give a popup if True, and just go to class otherwise
schedule = [
        {'class_name': 'example', 'time': 1100, 'days':['M','W','F'], 'url':'www.google.com', 'prompt':True},
        {'class_name': 'ex2', 'time': 1530, 'days':['T','TH'], 'url': '', 'prompt': True}
        #Add more here
]

f = open('schedule.json', 'w')
json.dump(schedule, f)
