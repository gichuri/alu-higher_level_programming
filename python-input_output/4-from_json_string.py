#!/usr/bin/python3
"""decoding json string to python object"""
import json


def from_json_string(my_str):
    """returning python object"""
    return json.loads(my_str)
