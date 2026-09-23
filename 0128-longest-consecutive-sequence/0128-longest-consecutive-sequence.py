class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        num_set = set(nums)

        longest = 0
        # with list it gives a TLE on case 81 because of duplicates values.
        for n in num_set:
            # if the n-1 is not in set then it means this can be a start of a sequence.
            if n-1 not in num_set:

                length = 0
                while (n+length) in num_set:
                    length += 1

                longest  = max(length, longest)

        return longest
        