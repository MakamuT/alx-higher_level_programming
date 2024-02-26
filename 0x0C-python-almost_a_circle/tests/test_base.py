#!/usr/bin/python3
'''Module for unittests for Rectangle class'''

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
    '''Tests for Base class'''

    def test_init_no_id(self):
        '''Test __init__ with no ID'''
        b1 = Base()
        assert isinstance(b1, Base)
        assert hasattr(b1, 'id')
        self.assertEqual (b1.id, 5)

        b2 = Base(None)
        b3 = Base(None)
        self.assertEqual(b2.id, b3.id - 1)

