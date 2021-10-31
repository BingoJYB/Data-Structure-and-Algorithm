#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (32.75%)
# Likes:    1389
# Dislikes: 2439
# Total Accepted:    205.3K
# Total Submissions: 624.8K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of strings words and a width maxWidth, format the text such
# that each line has exactly maxWidth characters and is fully (left and right)
# justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line does not divide evenly between words, the
# empty slots on the left will be assigned more spaces than the slots on the
# right.
# 
# For the last line of text, it should be left-justified and no extra space is
# inserted between words.
# 
# Note:
# 
# 
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["This", "is", "an", "example", "of", "text",
# "justification."], maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
# 
# Example 2:
# 
# 
# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth =
# 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified becase it contains only one
# word.
# 
# Example 3:
# 
# 
# Input: words =
# ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 300
# 1 <= words[i].length <= 20
# words[i] consists of only English letters and symbols.
# 1 <= maxWidth <= 100
# words[i].length <= maxWidth
# 
# 
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        import math

        c_count = 0
        w_count = 0
        spaces = []
        res = []
        
        for word in words:
            if c_count == 0:
                c_count = len(word)
                res.append([word])
                w_count += 1
            elif c_count + 1 + len(word) <= maxWidth:
                c_count += 1
                c_count += len(word)
                res[-1].append(word)
                w_count += 1
            else:
                if w_count > 1:
                    s_count = maxWidth - c_count + w_count - 1
                    avg_space = s_count // (w_count - 1)
                    space = [avg_space] * (w_count - 1)

                    for i in range(s_count % (w_count - 1)):
                        space[i] += 1
                else:
                    space = [maxWidth - len(res[-1][-1])]

                w_count = 1
                c_count = len(word)
                res.append([word])
                spaces.append(space[:])

        last = res[-1]
        width = maxWidth
        s_last = []
        for w in last:
            width -= len(w)

            if w == words[-1]:
                s_last.append(width)
            else:
                s_last.append(1)
                width -= 1

        spaces.append(s_last[:])

        for i, ws in enumerate(res):
            str = ""
            
            for w in ws:
                str += w

                if spaces[i]:
                    str += " " * spaces[i].pop(0)
            
            res[i] = str

        return res
# @lc code=end
