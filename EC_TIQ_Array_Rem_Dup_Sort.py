# October 25, 2021
# EC_TIQ_Array_Rem_Dup_Sort =
# Easy Collection
# Top Interview Questions
# Array type of question
# Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the
# duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some
# languages, you must instead have the result be placed in the first
# part of the array nums. More formally, if there are k elements after
# removing the duplicates, then the first k elements of nums should hold
# the final result. It does not matter what you leave beyond the
# first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by
# modifying the input array in -place with O(1) extra memory.

# https://www.python.org/dev/peps/pep-0008/#maximum-line-length
# the line length should be limited to 72 characters

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1
        return i + 1


# Runtime: 93 ms (48.43%)
# Memory Usage: 14.7 MB (65.23%)
