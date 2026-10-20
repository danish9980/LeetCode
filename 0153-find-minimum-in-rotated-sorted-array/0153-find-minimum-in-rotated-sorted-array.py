class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        arr = nums
        l = 0
        r = len(arr)-1

        while l<r:

            m = (l+r)//2

            # if arr[m] == target:
            #     return m

            # if arr[m] <= arr[-1]:
            #     l = m + 1

            # else:
            #     r = m

            if arr[m] <= arr[-1]:
                r = m
            else:
                l = m + 1
        # return value and not the index
        return nums[l]