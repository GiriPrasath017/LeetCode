class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        t1 = 2*(n-1)
        et = time%t1
        
        if et<n:
            return et+1
        else:
            return 2*n-et-1