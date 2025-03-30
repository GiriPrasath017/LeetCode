class Solution(object):
    def minBitFlips(self, start, goal):
        x = start^goal
        ans = 0
        
        while x > 0:
            ans += x&1  
            x >>= 1     
        
        return ans