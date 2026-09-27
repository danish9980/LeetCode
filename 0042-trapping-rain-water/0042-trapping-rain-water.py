class Solution:
    def trap(self, height: list[int]) -> int:

        # n = len(height)
        # l = 0
    
        # r = n-1

        # # leftwall = height[l]
        # # rightwall = height[r]

        # leftwall = height[l]
        # rightwall = height[r]

        # water  = 0

        # while l<r:
        #     if leftwall<rightwall:
        #         # we know here that the left wall is smaller.
        #         l +=1
        #         leftwall = max(leftwall, height[l])
        #         water = water + (leftwall - height[l])
                
                
        #     else:
        #         # we know here that rightwall is smaller.
        #         r -=1
        #         rightwall = max(rightwall, height[r])
        #         water = water + (rightwall - height[r])
                
        # return water


        n = len(height)

        leftmax_wall = [0] * n
        rightmax_wall = [0] * n
        
        leftmax_wall[0] = height[0]
        # go from left to right, forward
        for i in range(1, n):
            leftmax_wall[i]  = max(leftmax_wall[i-1], height[i])

        # go from right to left, backwards
        rightmax_wall[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            # print(i)
            rightmax_wall[i]  = max(rightmax_wall[i+1], height[i])

        water = 0
        for i in range(n):
            water = water + min(leftmax_wall[i] , rightmax_wall[i]) - height[i]

        return water