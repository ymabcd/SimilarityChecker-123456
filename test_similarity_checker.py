from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = SimilarityChecker()


    def test_strings_have_same_lengths(self):
        self.assertEqual(60, self.checker.string_length_comparison("ASD", "DSA"))

    def test_strings_have_different_lengths(self):
        result = self.checker.string_length_comparison("AAABB", "BAA")
        self.assertEqual(int((1 - 2 / 3) * 60), result)

        result = self.checker.string_length_comparison("AA", "AAE")
        self.assertEqual(int((1 - 1 / 2) * 60), result)

    def test_string_length_difference_exceeds_double(self):
        self.assertEqual(0, self.checker.string_length_comparison("A", "BB"))

    def test_strings_contain_same_letters(self):
        self.assertEqual(40, self.checker.alpha_comparison("ASD", "DSA"))

    def test_strings_have_unique_letters(self):
        self.assertEqual(0, self.checker.alpha_comparison("A", "BB"))

    def test_string_is_all_uppercase(self):
        self.assertEqual(40, self.checker.alpha_comparison("AAABB", "BAA"))

    def test_strings_contain_letters(self):
        self.assertEqual(20, self.checker.alpha_comparison("AA", "AAE"))

