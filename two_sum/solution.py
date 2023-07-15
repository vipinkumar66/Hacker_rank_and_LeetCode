# Solution 1

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        first_index = 0
        second_index =1
        length = len(nums)

        while first_index < length:
            if nums[first_index] + nums[second_index] == target:
                return [first_index, second_index]
            elif second_index < length-1:
                second_index+=1
            elif second_index == length-1:
                first_index+=1
                second_index = first_index + 1


# SOLUTION 2

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_table = {}
        for i, number in enumerate(nums):
            complement = target - number
            if complement in hash_table:
                return [hash_table[complement], i]
            hash_table[number] = i
        return []


