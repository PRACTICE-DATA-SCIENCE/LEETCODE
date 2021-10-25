# October 25, 2021
# EC_TIQ_Array_Rem_Dup_Sort =
# Easy Collection
# Top Interview Questions
# Array type of question
# 217. Contains Duplicate

# Given an integer array nums, return true if any value appears at
# least twice in the array, and return false if every element
# is distinct.
# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: true
# Example 2:
# Input: nums = [1, 2, 3, 4]
# Output: false
# Example 3:
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true
# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# Accepted # 1M # Submissions # 1.8M

# https://www.python.org/dev/peps/pep-0008/#maximum-line-length
# the line length should be limited to 72 characters

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

# Runtime: 96 ms (84.59%)
# Memory Usage: 19.3 MB (24.26%)
