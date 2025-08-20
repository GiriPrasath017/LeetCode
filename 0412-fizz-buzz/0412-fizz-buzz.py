from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        nr = []
        for i in range(1, n + 1):  
            if i % 3 == 0 and i % 5 == 0:
                nr.append("FizzBuzz")  
            elif i % 3 == 0:
                nr.append("Fizz")
            elif i % 5 == 0:
                nr.append("Buzz")
            else:
                nr.append(str(i))
        return nr
