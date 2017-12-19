# DO NOT MODIFY THIS FILE!!!

from unittest import TestCase  #, patch

from Lab_1.lab import q1


# @patch(input) # Eat any extra input statements. TODO fail if any are used?
class Q1Test(TestCase):

    def test_which_number_larger_same_numbers(self):

        msg = 'When called with %.1f and %.1f, which_number_is_larger() should return "same"'
        self.assertEqual('same', q1.which_number_is_larger(1.5, 1.5), msg=msg % (1.5, 1.5))
        self.assertEqual('same', q1.which_number_is_larger(-6, -6), msg=msg % (-6, -6))
        self.assertEqual('same', q1.which_number_is_larger(3, 3), msg=msg % (3, 3))
        self.assertEqual('same', q1.which_number_is_larger(-1000, -1000), msg=msg % (-1000, -1000))


    def test_which_number_larger_first_larger(self):

        msg = 'When called with %.1f and %.1f, which_number_is_larger() should return "first"'
        self.assertEqual('first', q1.which_number_is_larger(10, 2), msg=msg % (10, 2))
        self.assertEqual('first', q1.which_number_is_larger(-1, -100), msg=msg % (-1, -100))
        self.assertEqual('first', q1.which_number_is_larger(1, -100), msg=msg % (1, -100))
        self.assertEqual('first', q1.which_number_is_larger(5.5, 4.4), msg=msg % (5.5, 4.4))


    def test_which_number_larger_second_larger(self):

        msg = 'When called with %.1f and %.1f, which_number_is_larger() should return "first"'
        self.assertEqual('second', q1.which_number_is_larger(7, 20), msg=msg % (7, 20))
        self.assertEqual('second', q1.which_number_is_larger(-1, 100), msg=msg % (-1, 100))
        self.assertEqual('second', q1.which_number_is_larger(-100, -10), msg=msg % (-100, -10))
        self.assertEqual('second', q1.which_number_is_larger(20, 55.5), msg=msg % (20, 55.5))

