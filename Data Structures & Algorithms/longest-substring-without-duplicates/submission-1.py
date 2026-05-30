class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res=0

        for i in range(len(s)):

            charset=set()   # for every i updation create new set as every set is a substring
            for j in range(i,len(s)):

                if s[j] in charset:
                    break  # means update i
                else:
                    charset.add(s[j])
            res=max(res,len(charset))
        return res
        