class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def find_left(nums, target):
            l = 0
            r = len(nums)
            left_range = None

            while l<r:
                m =  l + (r-l) // 2


                if nums[m] == target:
                    left_range = m
                    r = m

                elif nums[m] < target:
                    l = m + 1
                
                else:
                    r = m

            
            return left_range
        
                    

        def find_right(nums, target):

            l = 0
            r = len(nums)
            right_range = None

            while l<r:
                m =  l + (r-l) // 2


                if nums[m] == target:
                    right_range = m
                    l = m + 1

                elif nums[m] < target:
                    l = m + 1
                
                else:
                    r = m
            
            return right_range

        
        left_boundry = find_left(nums, target)
        right_boundry = find_right(nums, target)

        if left_boundry is not None and right_boundry is not None:
            return [left_boundry, right_boundry]
        else:
            return [-1 , -1]
        