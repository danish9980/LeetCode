class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        # don't do off by one error.
        l = 1 
        r = max(piles)


        while l<r:
            m = l+ (r-l) //2 
            # m = (l+r)//2
            hours = 0
            for p in piles:
                hours = hours + math.ceil(p/m)
            
            if hours <= h:
                r = m
                # l = m+1
            else:
                # r = m
                l = m+ 1
        return r