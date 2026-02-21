class Solution:
    def reverse(self, nums: List[int],st: int, end: int) ->None:
        while st<end:
            nums[st], nums[end]= nums[end],nums[st]
            st+=1
            end-=1
    def rotate(self, nums: List[int], k: int) -> None:
        if k==0: return
        n=len(nums)
        k%=n
        #step 1 reverse entire list
        self.reverse(nums,o,n-1)
        #step 2 reverse the first k elements 
        self.reverse(nums,0,k-1)
        #reverse the remaning elements
        self.reverse(nums,k,n-1)
        

       
        