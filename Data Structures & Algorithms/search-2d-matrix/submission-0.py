class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) * len(matrix)-1
        cols = len(matrix[0])
        while l <= r:
            m= (l+r)//2
            rows = m // cols
            colms = m % cols
            #print(l,r,cols,m,rows,colms)
            #print(matrix[rows][colms])
            if matrix[rows][colms] == target:
                return True
            elif matrix[rows][colms] > target:
                r = m - 1
            elif matrix[rows][colms] < target:
                l = m + 1
        return False

