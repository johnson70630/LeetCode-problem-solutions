from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target, left, right = -nums[i], i+1, len(nums)-1
            while right > left:
                if nums[left] == nums[left-1] and left > i+1:
                    left += 1
                    continue
                total = nums[right] + nums[left]
                if total == target:
                    ans.append([nums[i], nums[right], nums[left]])
                    right -= 1
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    left += 1
        return ans
