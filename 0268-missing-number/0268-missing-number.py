class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nsum = n*(n+1)//2  
        ssum = 0
        for i in range(n):
            ssum = ssum+nums[i]
        return nsum-ssum  
