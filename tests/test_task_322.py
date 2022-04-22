""" Test of task_322.py """
from unittest import TestCase
from unittest import main

from task_322 import get_divisors_list
from task_322 import get_number_with_largest_sum_of_divisors


class TestGetDivisorsList(TestCase):
    """Tests for function: get_divisors_list"""

    def test_without_argument(self):
        """Test without function argument"""
        with self.assertRaises(TypeError):
            get_divisors_list()

    def test_with_zero_argument(self):
        """Test with 0 as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            get_divisors_list(0)
        self.assertEqual("Number should be greater than 0", test_exception.exception.args[0])

    def test_with_negative_argument(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            get_divisors_list(-1)
        self.assertEqual("Number should be greater than 0", test_exception.exception.args[0])

    def test_with_wrong_type_of_argument(self):
        """Test with not integer variables as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            get_divisors_list(1.7)
        self.assertEqual("Number should be integer", test_exception.exception.args[0])

        with self.assertRaises(AssertionError) as test_exception:
            get_divisors_list("15")
        self.assertEqual("Number should be integer", test_exception.exception.args[0])

        with self.assertRaises(AssertionError) as test_exception:
            get_divisors_list((5, 6, 7))
        self.assertEqual("Number should be integer", test_exception.exception.args[0])

        with self.assertRaises(AssertionError) as test_exception:
            get_divisors_list([5, 6, 7])
        self.assertEqual("Number should be integer", test_exception.exception.args[0])

    def test_with_multi_argument(self):
        """Test with too many function arguments"""
        with self.assertRaises(TypeError):
            get_divisors_list(5, 6, 7)
            get_divisors_list("5", "6", "7")
            get_divisors_list(5.1, "6", 7)

    def test_negative_result(self):
        """Test with negative result expectation"""
        self.assertNotEqual(get_divisors_list(16), [])
        self.assertNotEqual(get_divisors_list(133), [1])

    def test_positive_result(self):
        """Test with positive result expectation"""
        self.assertEqual(get_divisors_list(1), [])
        self.assertEqual(get_divisors_list(131), [1])
        self.assertEqual(get_divisors_list(16), [1, 2, 4, 8])


class TestGetNumberWithLargestSumOfDivisors(TestCase):
    """Tests for function: get_number_with_largest_sum_of_divisors"""
    def test_without_arguments(self):
        """Test without function argument"""
        self.assertRaises(TypeError, get_number_with_largest_sum_of_divisors)
        self.assertRaises(TypeError, get_number_with_largest_sum_of_divisors, 1)

    def test_with_zero_argument(self):
        """Test with 0 as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            get_number_with_largest_sum_of_divisors(0, 55)
        self.assertEqual("Number should be greater than 0", test_exception.exception.args[0])

    def test_with_negative_arguments(self):
        """Test with negative number as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            get_number_with_largest_sum_of_divisors(-1, 55)
        self.assertEqual("Number should be greater than 0", test_exception.exception.args[0])

        with self.assertRaises(AssertionError) as test_exception:
            get_number_with_largest_sum_of_divisors(-55, -1)
        self.assertEqual("Number should be greater than 0", test_exception.exception.args[0])

    def test_with_reversed_arguments(self):
        """Test with reversed range as function arguments"""
        with self.assertRaises(AssertionError) as test_exception:
            get_number_with_largest_sum_of_divisors(55, 1)
        self.assertEqual("Second (b) argument should be bigger than first (a)",
                         test_exception.exception.args[0]
                         )

        with self.assertRaises(AssertionError) as test_exception:
            get_number_with_largest_sum_of_divisors(-1, -55)
        self.assertEqual("Second (b) argument should be bigger than first (a)",
                         test_exception.exception.args[0]
                         )

    def test_with_wrong_type_of_arguments(self):
        """Test with not integer variables as function argument"""
        with self.assertRaises(AssertionError) as test_exception:
            get_number_with_largest_sum_of_divisors(1.7, 55)
        self.assertEqual("Boundaries (a and b) should be integers",
                         test_exception.exception.args[0]
                         )

        with self.assertRaises(AssertionError) as test_exception:
            get_number_with_largest_sum_of_divisors("1", "15")
        self.assertEqual("Boundaries (a and b) should be integers",
                         test_exception.exception.args[0]
                         )

        with self.assertRaises(AssertionError) as test_exception:
            get_number_with_largest_sum_of_divisors((5, 22), (5, 22))
        self.assertEqual("Boundaries (a and b) should be integers",
                         test_exception.exception.args[0]
                         )

        with self.assertRaises(AssertionError) as test_exception:
            get_number_with_largest_sum_of_divisors([5, 22], [5, 22])
        self.assertEqual("Boundaries (a and b) should be integers",
                         test_exception.exception.args[0]
                         )

    def test_with_multi_argument(self):
        """Test with too many function arguments"""
        with self.assertRaises(TypeError):
            get_number_with_largest_sum_of_divisors(5, 6, 7)
            get_number_with_largest_sum_of_divisors("5", "6", "7")
            get_number_with_largest_sum_of_divisors(5.1, "6", 7)

    def test_negative_result(self):
        """Test with negative result expectation"""
        self.assertNotEqual(get_number_with_largest_sum_of_divisors(1, 10), 5)
        self.assertNotEqual(get_number_with_largest_sum_of_divisors(111, 222), 100)

    def test_positive_result(self):
        """Test with positive result expectation"""
        self.assertEqual(get_number_with_largest_sum_of_divisors(1, 10), 8)
        self.assertEqual(get_number_with_largest_sum_of_divisors(111, 222), 106)


if __name__ == "__main__":
    main()
