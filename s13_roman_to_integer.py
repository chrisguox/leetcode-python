class Solution:
    def romanToInt(self, s: str) -> int:
        roman_number_dict = {
            "I": 1,
            # "IV": 4,
            "V": 5,
            # "IX": 9,
            "X": 10,
            # "XL": 40,
            "L": 50,
            # "XC": 40,
            "C": 100,
            # "CD": 400,
            "D": 500,
            # "DM": 900,
            "M": 1000,
        }

        spec_set = {
            "V": "I",
            "X": "I",
            "L": "X",
            "C": "X",
            "D": "C",
            "M": "C",
        }

        sum_nums = roman_number_dict[s[0]]

        for index, roman_num in enumerate(s):
            if index == 0:
                continue

            if roman_num in spec_set and s[index - 1] == spec_set[roman_num]:
                sum_nums += roman_number_dict[roman_num] - 2 * roman_number_dict[s[index - 1]]
            else:
                sum_nums += roman_number_dict[roman_num]

        return sum_nums
