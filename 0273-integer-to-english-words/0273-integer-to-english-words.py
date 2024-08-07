class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        places = ["", "Thousand", "Million", "Billion"]

        nw = ""
        pc = 0
        while num >0:
            if num%1000 != 0:
                y = num%1000
                h = y//100
                x = y%100
                nw3 =""
                if h>0:
                    nw3 += ones[h]+ " Hundred"

                if x> 0:
                    if h>0:
                        nw3 +=" "
                    if x<10:
                        nw3 += ones[x]
                    elif x<20:
                        nw3 += teens[x-10]
                    else:
                        nw3 += tens[x//10]
                        if x%10 > 0:
                            nw3 += " "+ones[x % 10]
                
                nw3 += " " +places[pc] + " "                
                nw = nw3 + nw
            num //=1000
            pc +=1

        return nw.strip()