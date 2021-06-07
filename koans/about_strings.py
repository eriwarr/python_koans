#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        # Strings in python are surrounded by either single quotation marks, or double quotation marks.
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        # Strings in python are surrounded by either single quotation marks, or double quotation marks.
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        # You can assign a multiline string to a variable by using three quotes
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        # You can assign a multiline string to a variable by using three quotes
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        # Python raw string is created by prefixing a string literal with ‘r’ or ‘R’.
        # Python raw string treats backslash (\) as a literal character.
        # This is useful when we want to have a string that contains backslash and don’t want it to be
        # treated as an escape character.
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        # we can use an escape sequence to insert a doubel quote.
        string = 'He said, "Go Away."'
        self.assertEqual('He said, \"Go Away.\"', string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        # We can use an escape sequence on a single quote.
        string = "Don't"
        self.assertEqual("Don\'t", string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        # This two are the same
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        # The len() function returns the number of items in an object or string.
        string = "It was the best of times,\n\
        It was the worst of times."
        self.assertEqual(60, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        # The length of the words plus the lines
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        # These are both the same
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        self.assertEqual('Hello "world"', string)

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual("Hello, world", string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)

    def test_most_strings_interpret_escape_characters(self):
        # The escape character is not counted in the length It tells the parser that the character following is printable, not a token.
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
