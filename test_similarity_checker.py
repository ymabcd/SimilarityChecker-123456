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
