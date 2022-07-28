#!/usr/bin/python3
"""write to text file in json string"""
import json


def save_to_json_file(my_obj, filename):
    """open txt file (with) and write using write"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
