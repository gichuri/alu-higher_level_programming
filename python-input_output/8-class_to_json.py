#!/usr/bin/python3
"""convert class to json"""


def class_to_json(obj):
    """return dict description of obj serialisation"""
    return obj.__dict__
