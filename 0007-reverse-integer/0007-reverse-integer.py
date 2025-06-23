class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            s = str(x)[1:]  
            rs = -int(s[::-1])  
        else:
            s = str(x)
            rs = int(s[::-1])  
        
        if rs < -2**31 or rs > 2**31 - 1:
            return 0
        
        return rs
