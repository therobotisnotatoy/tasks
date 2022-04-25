""" Test of task_88a.py """
from unittest import TestCase
from unittest import main

from tasks.task_88a import is_3_in_square_of_number



class TestIs3InSquareOfNumber(TestCase):
    """Tests for function: is_3_in_square_of_number"""

    def test_with_zero_argument(self):
        """Test with 0 as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            is_3_in_square_of_number(0)
        self.assertEqual("Number should be greater than 0", test_exception.exception.args[0])

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            is_3_in_square_of_number(-1)
        self.assertEqual("Number should be greater than 0", test_exception.exception.args[0])

    def test_negative_result(self):
        """Test with negative result expectation"""
        self.assertEqual(is_3_in_square_of_number(1), False)
        self.assertEqual(is_3_in_square_of_number(7), False)

    def test_positive_result(self):
        """Test with positive result expectation"""
        self.assertEqual(is_3_in_square_of_number(6), True)
        self.assertEqual(is_3_in_square_of_number(19), True)


if __name__ == "__main__":
    main()
