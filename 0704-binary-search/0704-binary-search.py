class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums)
        t =  target

        while l<r:
            # integer overflow
            # m =  (l+r)//2
            m = l+ (r-l) // 2

            # find the value in middle
            if nums[m] == target:
                return m

            if nums[m] < t:
                l = m + 1
            else:
                r = m

        return -1
        # neetcode 150