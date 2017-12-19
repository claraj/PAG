# DO NOT MODIFY THIS  FILE

from unittest import TestCase  #, patch

from Lab_1.lab import q2


# @patch(input) # Eat any extra input statements. TODO fail if any are used?
class Q2LengthTest(TestCase):

    def test_check_length_of_name_longer_than_6(self):

        msg = 'When called with %s, is_longer_than_6_letters() should return True"'
        name = 'Beyonce'  # 7 letters
        self.assertTrue(q2.is_longer_than_6_letters(name), msg=msg % name)

        name = 'Jacqueline Lee Kennedy Onassis'  # Way more than 6 letters
        self.assertTrue(q2.is_longer_than_6_letters(name), msg=msg % name)


    def test_check_length_of_name_6_letters(self):

        msg = 'When called with %s, is_longer_than_6_letters() should return False"'

        name = 'Barack'  # 6 letters
        self.assertFalse(q2.is_longer_than_6_letters(name), msg=msg % name)
        self.assertIsNotNone(q2.is_longer_than_6_letters(name), msg=msg % name)


        name = 'Gisele'  # 6 letters
        self.assertFalse(q2.is_longer_than_6_letters(name), msg=msg % name)
        self.assertIsNotNone(q2.is_longer_than_6_letters(name), msg=msg % name)



    def test_check_length_of_name_6_or_less(self):

        msg = 'When called with %s, is_longer_than_6_letters() should return False"'

        name = 'Kanye'  # less than 6 letters
        self.assertFalse(q2.is_longer_than_6_letters(name), msg=msg % name)
        self.assertIsNotNone(q2.is_longer_than_6_letters(name), msg=msg % name)

        name = 'Mia'  # less than 6 letters
        self.assertFalse(q2.is_longer_than_6_letters(name), msg=msg % name)
        self.assertIsNotNone(q2.is_longer_than_6_letters(name), msg=msg % name)


class Q2ShoutTest(TestCase):

    def test_shouting_lowercase(self):

        msg = 'When called with %s, shout() should return "%s" '

        name = 'beyonce'
        name_shout = 'BEYONCE!!!'
        self.assertEqual(name_shout, q2.shout(name), msg=msg % (name, name_shout))

        name = 'yoda'
        name_shout = 'YODA!!!'
        self.assertEqual(name_shout, q2.shout(name), msg=msg % (name, name_shout))


    def test_shouting_uppercase(self):

        msg = 'When called with %s, shout() should return "%s" '

        name = 'PIZZA'
        name_shout = 'PIZZA!!!'
        self.assertEqual(name_shout, q2.shout(name), msg=msg % (name, name_shout))


        name = 'VELOCIRAPTOR'
        name_shout = 'VELOCIRAPTOR!!!'
        self.assertEqual(name_shout, q2.shout(name), msg=msg % (name, name_shout))

