class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        # arr = nums
        # l = 0
        # r = len(arr)-1

        # # find the minimum in the mountain array.

        # # both pointers converge on same index.
        # while l<r:

        #     m = (l+r)//2

        #     if arr[m] < arr[m+1]:
        #         l = m +1

        #     else:
        #         r = m

        # return l

        





    

        l = 0 
        r = len(nums)-1

        while l < r:

            m = (l+r)//2

            if nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m

        return l
        # return m












        