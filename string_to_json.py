#!/usr/bin/python3

import json
from pathlib import Path

# get file
user_file = open(Path.home() / 'Code/Scripts/test_file.txt')

# create empty dictionary for usernames and passwords
credentials_dict = {'usernames':[], 'passwords':[]}

# iterate through words in file and append them to credentials_dict
for names in user_file:
    credentials_dict['usernames'].append(names.strip())
    credentials_dict['passwords'].append(names.strip())

# convert credentials_object into JSON data
credentials_object = json.dumps(credentials_dict, indent=2)

# print credentials_object
print(credentials_object)
