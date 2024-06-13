from collections import OrderedDict


class SimilarityChecker:

    def compare_same_length(self, first_length, second_length):
        return first_length == second_length

    def compare_string_exceeds_double(self, first_length, second_length):
        return first_length == second_length * 2 or second_length == first_length * 2

    def string_length_comparison(self, first_string, second_string):
        first_length = len(first_string)
        second_length = len(second_string)

        if self.compare_same_length(first_length, second_length):
            return 60

        if self.compare_string_exceeds_double(first_length, second_length):
            return 0

        a, b = (first_length, second_length) if first_length > second_length else (second_length, first_length)
        gap = a - b
        return int((1 - gap / b) * 60)

    def alpha_comparison(self, first_string, second_string):
        if len(first_string) == len(second_string):
            return 40

        temp = first_string + second_string
        unique_string = self.get_unique_characters(temp)
        totalCnt = len(unique_string)

        first_unique_string = self.get_unique_characters(first_string)
        second_unique_string = self.get_unique_characters(second_string)
        sameCnt = self.count_common_characters(first_unique_string, second_unique_string)

        return int(sameCnt / totalCnt * 40)

    def get_unique_characters(self, string):
        return list(OrderedDict.fromkeys(string))

    def count_common_characters(self, first_unique_string, second_unique_string):
        return len(set(first_unique_string) & set(second_unique_string))

