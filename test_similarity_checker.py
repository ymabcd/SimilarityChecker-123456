from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = SimilarityChecker()

    def test_strings_contain_same_letters(self):
        self.assertEqual(40, self.checker.alpha_comparison("ASD", "DSA"))

    def test_strings_have_unique_letters(self):
        self.assertEqual(0, self.checker.alpha_comparison("A", "BB"))

    def test_string_is_all_uppercase(self):
        self.assertEqual(40, self.checker.alpha_comparison("AAABB", "BAA"))

    def test_strings_contain_letters(self):
        self.assertEqual(20, self.checker.alpha_comparison("AA","AAE"))
