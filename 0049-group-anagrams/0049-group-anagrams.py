class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        ans = defaultdict(list)
        # temp_str = ""
        for s in strs:
            print(s)
            str_sorted = "a".join(sorted(s))
            print(str_sorted)
            print("----")

            ans[str_sorted].append(s)

        print(ans)
        print(ans.values())

        # return list(ans.values())

        print(type(ans))

        # final_ans = []
        # # for sorted_s, list_group in ans:
        # for sorted_s in ans:
        #     # final_ans.append(list_group)
        #     final_ans.append(ans[sorted_s])

        # return final_ans

        final_ans = []
        for sorted_s, list_group in ans.items():
            final_ans.append(list_group)
            # final_ans.append(ans[sorted_s])
            
        return final_ans



 
        