import unittest
from mathematics import max_number
from mathematics import descending_sorter


class TestList(unittest.TestCase):

    def test_max_number(self):
        assert max_number([3, 5, 9, 12, 78]) == 78, "the maximum number in mylist = to 78"

    def test_descending_sorter(self):
        assert descending_sorter([10, 6, 5, 18]) == [18, 10, 6, 5], "this is descending order"
