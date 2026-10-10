class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        r = 0
        l = len(nums)

        t = target
        n = nums

        while r < l:
            m = (r+l) //2
            if n[m] ==t:
                return m
            elif n[m] > t:
                l = m
            elif n[m] < t:
                r = m +1

        return r
        