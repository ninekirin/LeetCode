#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#

# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for record in operations:
            if record == 'C':
                records.pop()
            elif record == 'D':
                records.append(records[-1] * 2)
            elif record == '+':
                records.append(records[-1] + records[-2])
            else:
                records.append(int(record))

        return sum(records)
# @lc code=end

