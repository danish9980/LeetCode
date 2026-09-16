class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # top-most condition for the return
        # if k==1:
        #     # return list(set(nums))
        #     return nums

        # second portion of the algo
        # num = list = iterable = iterator
        # counts = Counter(nums)
        # key
        # val

        # print(counts)
        # print(counts[0])

        # my assumtion was that counter will return the sorted dictionary
        # ans = []
        # counter = 0
        # for c in counts:
        #     # ans.append(counts[c])
        #     ans.append(c)
        #     counter +=1
        #     if counter >=2:
        #         break
        # return ans

        
        counts = Counter(nums)
        counts_sorted = counts.most_common(k)
        return [key for key, val in counts_sorted]
        # list slicing
        # ans = []
        # for key, val in counts_sorted:
        #     ans.append(key)
        # return ans





        


             