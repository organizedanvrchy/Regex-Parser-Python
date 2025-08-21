import unittest
from regex_parser import re_parse

class TestRegexParser(unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(re_parse(""))

    def test_dot(self):
        self.assertEqual(re_parse("."), "dot")

    def test_single_char(self):
        self.assertEqual(re_parse("a"), "a")

    def test_concat(self):
        self.assertEqual(re_parse("ab"), ("cat", "a", "b"))

    def test_alternation(self):
        self.assertEqual(re_parse("a|b"), ("split", "a", "b"))

    def test_plus(self):
        self.assertEqual(re_parse("a+"), ("repeat", "a", 1, float("inf")))

    def test_repeat_range(self):
        self.assertEqual(re_parse("a{3,6}"), ("repeat", "a", 3, 6))

    def test_nested_alt(self):
        self.assertEqual(re_parse("a|bc"), ("split", "a", ("cat", "b", "c")))

if __name__ == "__main__":
    unittest.main()
