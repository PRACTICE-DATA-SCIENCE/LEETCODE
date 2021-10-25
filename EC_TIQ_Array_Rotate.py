# October 25, 2021
# EC_TIQ_Array_Rem_Dup_Sort =
# Easy Collection
# Top Interview Questions
# Array type of question
# 189. Rotate Array

# Given an array, rotate the array to the right by k steps,
# where k is non-negative.
# Example 1:
# Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]
# Explanation:
# rotate 1 steps to the right: [7, 1, 2, 3, 4, 5, 6]
# rotate 2 steps to the right: [6, 7, 1, 2, 3, 4, 5]
# rotate 3 steps to the right: [5, 6, 7, 1, 2, 3, 4]
# Example 2:
# Input: nums = [-1, -100, 3, 99], k = 2
# Output: [3, 99, -1, -100]
# Explanation:
# rotate 1 steps to the right: [99, -1, -100, 3]
# rotate 2 steps to the right: [3, 99, -1, -100]
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105
# Follow up:
# Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
# Could you do it in -place with O(1) extra space?
# Accepted 833.3K # Submissions 2.2M

# https://www.python.org/dev/peps/pep-0008/#maximum-line-length
# the line length should be limited to 72 characters

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # remove complete rotations
        if len(nums) > 1 and k >= 1:
            if k > len(nums):
                k = k % len(nums)
            # else:
            #     k_ = k
            # tail_2h = nums[-k_:] # to become [:k]
            # head_2t = nums[:-k_] # to become [k:]
            # nums[:k_] = tail_2h
            # nums[k_:] = head_2t

        # if k > len(nums):
        #     k = k % len(nums)

            nums[:] = nums[-k:] + nums[:-k]


# Runtime: 277 ms (23.86%)
# Memory Usage: 25 MB (39.32%)
