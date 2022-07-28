#!/usr/bin/python3
"""converting json file to python object"""
import json


def load_from_json_file(filename):
    """using load to convert json to python"""
    with(filename) as f:
        return json.load(f)
