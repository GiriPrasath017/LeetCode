class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        lr = 0
        maxln = 0
        
        for rg in range(len(fruits)):
            count[fruits[rg]] = count.get(fruits[rg], 0) + 1
            
            while len(count) > 2:
                count[fruits[lr]] -= 1
                if count[fruits[lr]] == 0:
                    del count[fruits[lr]]
                lr += 1  
            maxln = max(maxln, rg - lr + 1)
        
        return maxln
