#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (41.21%)
# Likes:    13697
# Dislikes: 307
# Total Accepted:    1.2M
# Total Submissions: 2.8M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# 
# Example 1:
# 
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
# 
# 
#

# @lc code=start
import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [math.inf] * amount
        
        for i in range(1, amount+1):
            dp[i] = min(dp[i-coin] if i-coin >= 0 else math.inf for coin in coins) + 1
            
        return -1 if dp[amount] == math.inf else dp[amount]
# @lc code=end

