#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 先按基数从大到小排列数，再根据数的第二位、第三位从大到小排序，如果基数相同而别的数位数更多，则更大的数排在前面
        # 例如：[3, 30, 34, 5, 9]，先按基数从大到小排列，得到[9, 5, 3, 30, 34]，再根据数的第二位、第三位从大到小排序，得到[9, 5, 34, 30, 3]
        maxDigit = 0
        for num in nums:
            maxDigit = max(maxDigit, len(str(num)))
        # str(x) * maxDigit 保证了基数相同的数，数位数更多的数排在前面
        nums = sorted(nums, key=lambda x: str(x) * maxDigit, reverse=True)
        return str(int(''.join(map(str, nums))))
# @lc code=end
