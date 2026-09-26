class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # l = 0
        # a = set()
        # lmax = 0
        # for i in range(len(s)):
        #     while s[i] in a:
        #         a.remove(s[l])
        #         l +=1

        #     a.add(s[i])
        #     lmax = max(lmax , (i-l)+1)

        # return lmax

        # second one
        l = 0
        a = {}
        lmax = 0
        for i in range(len(s)):

            if s[i] in a:
                l = max(l , a[s[i]]+1)

            a[s[i]] = i

            lmax = max(lmax , (i-l)+1)

        return lmax