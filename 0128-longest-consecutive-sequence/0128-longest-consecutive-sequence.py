class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        num_set = set(nums)

        longest = 0
        for n in num_set:
            # if the n-1 is not in set then it means this can be a start of a sequence.
            if n-1 not in num_set:

                length = 0
                while (n+length) in num_set:
                    length += 1

                longest  = max(length, longest)

        return longest
        