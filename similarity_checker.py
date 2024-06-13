class SimilarityChecker:
    def alpha_comparison(self, first_string, second_string):
        if len(first_string) == len(second_string):
            return 40

        temp = first_string + second_string
        unique_string = self.get_unique_characters(temp)
        totalCnt = len(unique_string)

        first_unique_string = self.get_unique_characters(first_string)
        second_unique_string = self.get_unique_characters(second_string)
        sameCnt = self.count_common_characters(first_unique_string, second_unique_string)

        return int(sameCnt/totalCnt*40)

    def get_unique_characters(self, string):
        seen = set()
        result = []
        for char in string:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return result

    def count_common_characters(self, first_unique_string, second_unique_string):
        common_count = 0
        for char in first_unique_string:
            if char in second_unique_string:
                common_count += 1
        return common_count
