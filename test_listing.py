import unittest
from listing import max_number


class TestList(unittest.TestCase):

    def test_max_number(self):
        assert max_number([3, 5, 9, 12, 78]) == 78, "The maximum number in my list is equal to 78"

