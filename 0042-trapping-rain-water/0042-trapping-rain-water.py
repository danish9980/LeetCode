class Solution:
    def trap(self, height: list[int]) -> int:

        n = len(height)
        left = 0
        right = n-1

        leftwall =  0
        rightwall = 0

        total_water = 0
        while left<=right:
            if leftwall < rightwall:
                # if right wall is greater then we know that that left wall is smaller and hence we take the max height of that wall to keep the leftwall updated.
                leftwall = max(leftwall, height[left])
                total_water = total_water + leftwall - height[left]
                left+=1
               
            else:
                # if leftwall < rightwall:
                rightwall = max(rightwall , height[right])
                total_water = total_water + rightwall - height[right]
                right-=1
                
        return total_water



