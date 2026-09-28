class Solution:
    def fib(self, n: int) -> int:

        # calcualate the nth fibonacci series number. 
        # but why we do it?
        # who was fibonacci

        if n==0:
            return 0

        if n==1:
            return 1 

            # 0 ,1 
        a = [0,1]

        # range misses the last value. 
        for i in range(2,n+1):
            a.append(a[i-2] + a[i-1])
        
        return a[-1]



        