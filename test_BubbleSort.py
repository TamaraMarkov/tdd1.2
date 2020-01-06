import unittest
import BubbleSort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        # stub
        stub_arr = [22, 11, 4, 12, 45]
        # assume
        expected1 = [4,11,12,22,45]
        # action
        result1 = BubbleSort.bubbleSort(stub_arr)
        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(len(expected1),len(result1))
        self.assertIsNotNone(result1, expected1)