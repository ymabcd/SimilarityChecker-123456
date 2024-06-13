from unittest import TestCase

from similarity_checker import SimilarityChecker


class TestSimilarityChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = SimilarityChecker()

    def test_strings_have_same_lengths(self):
        self.assertEqual(60, self.checker.string_length_comparison("ASD", "DSA"))

    def test_strings_have_different_lengths(self):
        # 긴 문자
        # 짧은 문자
        pass

    def test_string_length_difference_exceeds_double(self):
        self.assertEqual(0, self.checker.string_length_comparison("A", "BB"))
