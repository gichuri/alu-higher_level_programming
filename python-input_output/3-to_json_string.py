#!/usr/bin/python3
"""function to return Json representaion of an object"""


def to_json_string(my_obj):
    """return converted json string"""
    return json.dump(my_obj)
