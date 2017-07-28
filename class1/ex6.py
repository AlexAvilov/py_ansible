#!/usr/bin/env python

import yaml 
import json
import ciscoconfparse

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

print yaml.dump(my_list, default_flow_style=False)

