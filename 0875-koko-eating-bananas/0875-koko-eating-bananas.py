class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

    #    0, 
    #    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
     #    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12
    # ( 1, 11 ]
    # [1, 11)

        # min speed of koko
        l = 1
        # max speed of koko
        r = max(piles) + 20

        # terminate l == r
        # loop invariant
        # premise (predicate)
        # maintainence
        # termination
        while l < r:
            
            # 7.5 , floor division
            # ceil
            m = (l+r) // 2

            total_hours_needed_to_complete_all_the_piles_within_h = 0
            for p in piles:
                # floor
                total_hours_needed_to_complete_all_the_piles_within_h += ceil(p/m)
            
            if total_hours_needed_to_complete_all_the_piles_within_h <= h:
                r = m
            
            else:
                l = m+1

        return l

        # f f f f f f f f f t t t t t t t t t 
        # bridge will break
        