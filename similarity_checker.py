class SimilarityChecker:
    def compare_same_length(self, first_length, second_length):
        return first_length == second_length

    def compare_string_exceeds_double(self, first_length, second_length):
        if self.compare_same_length(first_length, second_length * 2) or self.compare_same_length(second_length,
                                                                                                 first_length * 2):
            return True
        return False

    def string_length_comparison(self, first_string, second_string):
        first_length = len(first_string)
        second_length = len(second_string)

        if self.compare_same_length(first_length, second_length):
            return 60

        if self.compare_string_exceeds_double(first_length, second_length):
            return 0

        a, b = (first_length, second_length) if first_length > second_length else (second_length, first_length)
        gap = a - b
        return int((1 - gap/b)*60)
