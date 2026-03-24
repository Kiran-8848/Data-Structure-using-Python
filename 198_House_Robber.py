class Solution:
    def rob(self, nums: List[int],) -> int:
        ans=0
        dp=dict()
        def f(nums, ind):

            if ind>=len(nums):
                return 0
            skip=f(nums,ind+1)
            take=nums[ind]+f(nums,ind+2)
            return max(skip,take)
        return f(nums, 0)