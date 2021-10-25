# October 25, 2021
# EC_TIQ_Array_Rem_Dup_Sort =
# Easy Collection
# Top Interview Questions
# Array type of question
# 136. Single Number

# Given a non-empty array of integers nums, every element appears twice
# except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use
# only constant extra space.

# https://www.python.org/dev/peps/pep-0008/#maximum-line-length
# the line length should be limited to 72 characters

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Runtime: 9188 ms, Memory Usage: 15.5 MB
        # for i in range(len(nums)-1):
        #     if nums[i] not in nums[:i] + nums[i+1:]:
        #         return nums[i]
        # return nums[-1] # last element unique

        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                return nums[i]
            else:
                i += 2
        return nums[-1]  # last element unique

# Runtime: 112 ms (71.47 %)
# Memory Usage: 15.6 MB (71.26)
