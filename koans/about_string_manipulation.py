#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        # The format() method formats the specified value(s) and insert them inside the string's placeholder.
        # The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
        # The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string)

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

    def test_any_python_expression_may_be_interpolated(self):
        # Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.
        import math # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual("The square root of 5 is 2.2361", string)

    def test_you_can_get_a_substring_from_a_string(self):
        # string[start: end: step]
        # Starts at the index indicated and ends at the index indicated.
        string = "Bacon, lettuce and tomato"
        self.assertEqual("let", string[7:10])

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("a", string[1])

    def test_single_characters_can_be_represented_by_integers(self):
        # The ord() function returns the number representing the unicode code of a specified character.
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

    def test_strings_can_be_split(self):
        # The split() method splits a string into a list. You can specify the separator, default separator is any whitespace.
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(['Sausage', 'Egg', 'Cheese'], words)

    def test_strings_can_be_split_with_different_patterns(self):
        # A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
        # RegEx can be used to check if a string contains the specified search pattern.
        # Python has a built-in package called re, which can be used to work with Regular Expressions.
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        self.assertListEqual(['the', 'rain', 'in', 'spain'], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual('\\n', string)
        self.assertEqual(2, len(string))

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        # The join() method takes all items in an iterable and joins them into one string.
        words = ["Now", "is", "the", "time"]
        self.assertEqual("Now is the time", ' '.join(words))

    def test_strings_can_change_case(self):
        self.assertEqual("Guido", 'guido'.capitalize())
        self.assertEqual("GUIDO", 'guido'.upper())
        self.assertEqual("timbot", 'TimBot'.lower())
        self.assertEqual("Guido Van Rossum", 'guido van rossum'.title())
        self.assertEqual("tOtAlLy AwEsOmE", 'ToTaLlY aWeSoMe'.swapcase())
