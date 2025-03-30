class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        mlen = 0
        cset = set()
        l = 0
        
        for i in range(n):
            if s[i] not in cset:
                cset.add(s[i])
                mlen = max(mlen, i - l + 1)
            else:
                while s[i] in cset:
                    cset.remove(s[l])
                    l += 1
                cset.add(s[i])
        
        return mlen