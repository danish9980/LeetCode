class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # ans = []
        # for idx, val in enumerate(nums):
        #     mul = 1
        #     for idx2, val2 in enumerate(nums):
        #         if idx != idx2:
        #             mul = mul * val2
        #     ans.append(mul)
        # print(ans)

        # return ans
        n = len(nums)
        ans = [0] * n
        print(ans)
        # single forward pass for prefix
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

            # prefix = prefix * ans[i]

        # single backward pass for suffix
        suffix =1
        for i in range(n-1, -1 , -1):
            ans[i] *= suffix
            suffix *= nums[i]
        
        return ans
            
       


            
        

            

        