class Solution:
    """
    利用map(dict)做处理，时间复杂度为 O(n);
    """
    def twoSum(self, nums, target):
        nums_dict = {}
        for index, num in enumerate(nums):
            addend = target - num
            if addend not in nums_dict:
                nums_dict[num] = index
                continue
            return [nums_dict[addend], index]
