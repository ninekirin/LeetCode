#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict = {}
        for i in range(len(s) - 9):
            if s[i:i + 10] in dict:
                dict[s[i:i + 10]] += 1
            else:
                dict[s[i:i + 10]] = 1
        return [key for key, value in dict.items() if value > 1]
# @lc code=endZ