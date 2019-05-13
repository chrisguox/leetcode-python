class Solution:
    """
    哨兵，记录重复字符的位置，往后继续计算下一个子串；
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string_dict = {}
        max_len = 0
        start = -1

        for index, word in enumerate(s):
            word = ord(word)
            if word in sub_string_dict and sub_string_dict[word] > start:
                start = sub_string_dict[word]

            current_max_len = index - start
            if current_max_len > max_len:
                max_len = current_max_len

            sub_string_dict[word] = index

        return max_len
