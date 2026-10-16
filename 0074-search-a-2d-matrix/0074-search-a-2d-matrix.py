class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # asceding order
        # all rows are in increasing order. 
        # -1 false return or 1 true.
        # monotic, increasing order ya phir decreasing order me.
        # data cleaning, find the range and then do the computation.
        # range queries bhi kehte hai.
        # binary search on data type that is distinct.
        # binary search on repeating data in the structure.
        # find the list (row where we have to search.)
        # or directly apply the binary search on each row. if found exit, if not search more till the last row. if not find till the last row return false.
        # send the indexes rather than the direct list.

        # does this even use auxiluary space.
        # agar me isko andar likh do to kya yeh extra space use karega ya nahi karega.
        # why we use 2d arrays mostly in machine learning rather than 2d list.
        # what are the professional variable names we can use in this question.
        # <= equal to and not equal to.

        # def binary_search(row_arr, t):

        #     l = 0
        #     r = len(row_arr)

        #     while l<r:
        #         m = (l+r)//2
        #         if row_arr[m] == t:
        #             return True

        #         # right me jao
        #         if row_arr[m] < t:
        #             l = m + 1
                
        #         # left me jao
        #         # why not m-1
        #         if row_arr[m] > t:
        #             r = m

        #     return False

        # t = target
        # m = len(matrix)
        # # print(m)
        # # it will go to all rows.
        # for i in range(m):
        #     row_arr = matrix[i]
        #     row_length = len(row_arr)
        #     check = binary_search(row_arr, t)
        #     # print(row_length)

        #     # if true
        #     if check:
        #         return check
        
        # return check

        #     # this is coarse boundry.
        #     # boundry ko loose rakhna hota hai.
        #     # what about & 
        #     # if row_arr[0] < t and row_arr[-1] > t:
        #     #     continue


        #     # continue

        # # return False

        l = 0
        # but what is this was not a square 2d array
        n_rows = len(matrix)
        # assuming that all rows have equal length
        n_cols = len(matrix[0])

        r = (n_rows  * n_cols ) - 1

        while l <= r:

            m = (l + r)//2

            row = m // n_cols
            col = m % n_cols

            val = matrix[row][col]

            # is it necessory to put multiple if branches here?
            if val == target:
                return True
            
            if val < target:
                l = m+1

            if val > target:
                r = m - 1 
            
        return False    