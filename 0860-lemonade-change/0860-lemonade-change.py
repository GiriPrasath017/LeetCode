class Solution:
    def lemonadeChange(self, bills):
        x = 0
        y = 0
        
        for i in bills:
            if i == 5:
                x += 1
            elif i == 10:
                if x == 0:
                    return False
                x -= 1
                y += 1
            else:  
                if y >= 1 and x >= 1:
                    y -= 1
                    x -= 1
                elif x >= 3:
                    x -= 3
                else:
                    return False
        return True