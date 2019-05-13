class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse_int = 0
        while reverse_int < x:
            reverse_int = reverse_int * 10 + x % 10
            x //= 10

        is_palindrome_number = reverse_int == x or reverse_int // 10 == x
        return is_palindrome_number
