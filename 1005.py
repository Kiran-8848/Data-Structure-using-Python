class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for _ in range(k):
            min_idx=0
            for i in range(1,len(nums)):
                if nums[i]<nums[min_idx]:
                    min_idx=i
            nums[min_idx] = -nums[min_idx]
        return sum(nums)
        