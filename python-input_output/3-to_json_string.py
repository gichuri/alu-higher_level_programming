#!/usr/bin/python3
"""function to return Json representaion of an object"""
import json


def to_json_string(my_obj):
    """return converted json string"""
    return json.dumps(my_obj)
