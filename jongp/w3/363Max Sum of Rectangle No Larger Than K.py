#hint from previous problem
from sortedcontainers import SortedList
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m,n=len(matrix),len(matrix[0])
        prefixSum=self.getPrefixSum(matrix)
        res=-math.inf
        
        
        
        for i in range(m-1,-1,-1):
            for ii in range(i,-1,-1):
                arry=SortedList([0])
                total=0
                for j in range(n):
                    cur=prefixSum[ii][j]-prefixSum[i+1][j]
                    
                    total+=cur
                    idx=arry.bisect_left(total-k)#have to study
                    if idx<len(arry) and res<total-arry[idx]:
                        res=total-arry[idx]
                    
                    arry.add(total)
                    
        
        
        return res
    
    
    
    
    
        
        
    def getPrefixSum(self,matrix):
        m,n=len(matrix),len(matrix[0])
        res=[[0]*n for _ in range(m+1)]
        
        
        for i in range(m-1,-1,-1):
            for j in range(n):
                res[i][j]=res[i+1][j]+matrix[i][j]
        
        
        return res