from bisect import bisect_left
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in matrix :
            if i[0]<=target<=i[m-1] :
                a = bisect_left(i,target)
                if a!= m and i[a] == target :
                    return True
        return False
