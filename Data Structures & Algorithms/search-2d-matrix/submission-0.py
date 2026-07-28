class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if not matrix or not matrix[0]:
            return False

        row=len(matrix)
        col=len(matrix[0])
        l=0
        h=row*col -1

        while l<=h:
            m=l+(h-l)//2

            r = m//col
            c = m%col

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                l=m+1
            else:
                h=m-1
        return False