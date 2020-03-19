#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (30.65%)
# Likes:    1627
# Dislikes: 527
# Total Accepted:    316.3K
# Total Submissions: 1M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        result = 0
        isChecked = [False] * n

        for num in range(2, n):
            if not isChecked[num]:
                base = 2
                result += 1
                isChecked[num] = True
                maybe_prime = num * base

                while maybe_prime < n:
                    isChecked[maybe_prime] = True
                    base += 1
                    maybe_prime = base * num

        return result

# @lc code=end

