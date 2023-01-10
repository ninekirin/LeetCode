#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 三指针
        # 1. left指针指向0的右边界，right指针指向2的左边界
        # 2. 从left开始遍历，如果遇到0，则与left交换，left右移；如果遇到2，则与right交换，right左移；如果遇到1，则left右移
        # 3. 直到left >= right
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1
        
# @lc code=end

