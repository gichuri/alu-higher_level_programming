#!/usr/bin/python3
"""convert class to json"""
import json


def class_to_json(obj):
    """return dict description of obj serialisation"""
    return json.load(obj)
