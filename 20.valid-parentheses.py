#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in ['(', '[', '{']:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if bracket == ')' and stack[-1] != '(':
                    return False
                if bracket == ']' and stack[-1] != '[':
                    return False
                if bracket == '}' and stack[-1] != '{':
                    return False
                stack.pop()
        return not stack
# @lc code=end

