class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        a = defaultdict(int)
        l = 0
        max_char_count = 0
        _len = 0
        for i in range(len(s)):
            
            a[s[i]] += 1
            # wrong, this is assingment of the value
            # a[s[i]] =+ 1
            max_char_count = max(max_char_count, a[s[i]])

            # check the window is valid or not
            if ((i-l)+1) - max_char_count <= k:
                _len +=1

            else:
                # decrease the count of the character from the left side.
                a[s[l]] -= 1
                l +=1

        return _len




                    






        

        