#!/usr/bin/python3
import unittest
import 6-max_integer.py

class TestName(unittest.TestCase):

   def test_name(self):
       self.assertEquals(6-max_integer.max_integer(list=[1,2,3,4]), 4)
       self.assertEquals(6-max_integer.max_integer(list=[11,2,3,4]), 11)
       self.assertEquals(6-max_integer.max_integer(list=[1,2,78,9]), 78)
       self.assertEquals(6-max_integer.max_integer(list=[1, -2, 78, 9]), 78)
       self.assertEquals(6-max_integer.max_integer(list=[-1, -2, -78, -9]), -1)
       self.assertEquals(6-max_integer.max_integer(list=[78]), 78)
       self.assertEquals(6-max_integer.max_integer(list=[]), None)
