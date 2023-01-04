#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # check length
        if len(s) != len(t):
            return False
        # check isomorphic
        dict = {}
        for i in range(len(s)):
            # s[i] in dict, check if dict[s[i]] == t[i]
            if s[i] in dict:
                if dict[s[i]] != t[i]:
                    return False
            # s[i] not in dict, check if t[i] in dict.values()
            else:
                if t[i] in dict.values():
                    # because s[i] not in dict, so t[i] must not in dict.values()
                    return False
                dict[s[i]] = t[i]
        return True
# @lc code=end