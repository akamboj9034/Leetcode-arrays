class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(nums, start, end):
            if start == end:
                return nums[start], nums[start], nums[start], nums[start]
            else:
                mid = start + (end - start)//2
                
                left_ans , left_maxFromBeginning , left_maxFromEnd , left_totalSum  = helper(nums, start, mid)
                right_ans, right_maxFromBeginning, right_maxFromEnd, right_totalSum = helper(nums, mid+1, end)
                
                ans = max(left_ans, right_ans, left_maxFromEnd + right_maxFromBeginning)
                maxFromBeginning = max(left_maxFromBeginning, left_totalSum + right_maxFromBeginning)
                maxFromEnd = max(right_maxFromEnd, right_totalSum + left_maxFromEnd)
                totalSum = left_totalSum + right_totalSum
                
            return (ans, maxFromBeginning, maxFromEnd, totalSum)
        
        ans, _, _, _ = helper(nums, 0, len(nums)-1)
        return ans