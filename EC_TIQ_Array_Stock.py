# October 25, 2021
# EC_TIQ_Array_Rem_Dup_Sort =
# Easy Collection
# Top Interview Questions
# Array type of question
# 122. Best Time to Buy and Sell Stock II

# You are given an integer array prices where prices[i] is the price of
# a given stock on the ith day.
# On each day, you may decide to buy and / or sell the stock. You can
# only hold at most one share of the stock at any time. However, you can
# buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
# Example 1:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 7
# Explanation: Buy on day 2 (price=1) and sell on day 3 (price=5), profit = 5-1 = 4.
# Then buy on day 4 (price=3) and sell on day 5 (price=6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
# Example 2:
# Input: prices = [1, 2, 3, 4, 5]
# Output: 4
# Explanation: Buy on day 1 (price=1) and sell on day 5 (price=5), profit = 5-1 = 4.
# Total profit is 4.
# Example 3:
# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
# Constraints:
# 1 <= prices.length <= 3 * 104
# 0 <= prices[i] <= 104
# Accepted 971.4K
# Submissions 1.6M

# https://www.python.org/dev/peps/pep-0008/#maximum-line-length
# the line length should be limited to 72 characters

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # import numpy as np
        # p = np.array(prices)
        # p_diff = p[1:] - p[0:-1]
        # filter = p_diff > 0
        # # profit = sum(p_diff[filter])
        # return sum(p_diff[filter])

        # cedit: Easiest Approch  O(n) 2-liner
        # Shivam_007's avatar September 21, 2021 8:36 AM 41 VIEWS
    	# if prices==0:return 0
    	# return sum(prices[i]-prices[i-1] for i in range(1,len(prices))
        # if prices[i-1]<prices[i])

        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i]-prices[i-1]
        return res
