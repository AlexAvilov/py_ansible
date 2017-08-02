#!/usr/bin/env python

import yaml 
import json
import ciscoconfparse
from pprint import pprint as pp

def create_list():
    my_list = range(6)
    my_list.append("text")
    my_list.append("more text")
    my_list.append({})
    my_list[-1]["one"] = 1
    my_list[-1]["two"] = 2
    my_list[-1][2] = 'two'
    my_list[-1][1] = 'one'
    my_list[-1]['digit'] = range(10)
    
    return( my_list)

my_list = create_list()

# YAML
# print yaml.dump(my_list, default_flow_style=False)

with open("ex6.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open("ex6-1.yml", "w") as f:
    yaml.dump(my_list, f)


# json
# print json.dumps(my_list)

with open("ex6.json", "w") as f:
    json.dump(my_list,f)



with open("ex6.yml") as f:
    y_list = yaml.load(f)

    pp(y_list)

with open("ex6-1.yml") as f:
    y_list = yaml.load(f)

    pp(y_list)



with open("ex6.json") as f:
    j_list = json.load(f)

    pp(j_list)

