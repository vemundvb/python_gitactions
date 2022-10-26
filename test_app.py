import unittest
import pytest

from app import Two
#asd
class TestIsTwo(unittest.TestCase):
    def test_two_is_two(self):
        result = Two(2)
        assert result.number == 2

class TestIsNotTwo(unittest.TestCase):
    def test_two_is_two(self):
        result = Two(3)
        assert result.number != 3



