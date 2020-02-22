class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = runningSum = nums[0]
        for i in range(1, len(nums)):
            runningSum = max(nums[i], nums[i]+runningSum)
            ans = max(ans, runningSum)
        return ans