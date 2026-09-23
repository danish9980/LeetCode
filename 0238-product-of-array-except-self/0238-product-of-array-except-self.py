class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        pre_array = [1] * n
        post_array = [1] * n
        res = [1] * n

        prefix = 1 
        for i in range(n):
            pre_array[i] = prefix
            prefix *= nums[i]
        
        postfix= 1
        for i in range(n-1, -1 , -1):
            post_array[i] = postfix
            postfix *= nums[i]

        for i in range(n):
            res[i] = pre_array[i] * post_array[i]

        return res


        