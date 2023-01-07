#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        max_area = 0
        # i is the width of the rectangle
        # j is the starting index of the rectangle
        # 注意 range 右侧的 +1，因为 range 不包含右侧的值（开区间）
        for i in range(1, len(heights) + 1):
            for j in range(len(heights) - i + 1):
                area = min(heights[j:j+i]) * i
                if area > max_area:
                    max_area = area
        return max_area
# @lc code=end