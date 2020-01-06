import unittest
import bmi

class bmiTest(unittest.TestCase):
    def test_Bmi_Calc(self):
        # stub
        stub_height = 1.75
        stub_weight= 64
        # assume
        expected1 = 20.897959183673468

        # action
        result1 = bmi.Bmi_Calc(stub_height, stub_weight)

        # expect/assert
        self.assertEqual(result1, expected1)

    def test_Bmi_Status(self):
        # stub
        stub_bmi = 17
        # assume
        expected1 = "underweight"

        # action
        result1 = bmi.Bmi_Status(stub_bmi)

        # expect/assert
        self.assertEqual(result1, expected1)

if __name__ == '__main__':
    unittest.main()
