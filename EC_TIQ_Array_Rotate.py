# October 25, 2021
# EC_TIQ_Array_Rem_Dup_Sort =
# Easy Collection
# Top Interview Questions
# Array type of question
# 189. Rotate Array

# You are given an integer array prices where prices[i] is the price of
# a given stock on the ith day.
# On each day, you may decide to buy and / or sell the stock. You can
# only hold at most one share of the stock at any time. However, you can
# buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.

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
