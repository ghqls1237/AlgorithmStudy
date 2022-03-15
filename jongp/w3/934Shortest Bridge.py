from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        que=self.init(grid)
        
        return self.bfs(grid,que)
    

    
    def init(self,grid):
        n=len(grid)
        que=deque([])
        flag=False
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    if flag:
                        que.append((i,j))
                    else:
                        self.setDest(grid,i,j)
                        flag=True
        return que


    
    def bfs(self,grid,que):
        step=0
    
        while que:
            for _ in range(len(que)):
                cx,cy=que.popleft()
                
                for nx,ny in self.nextCoor(len(grid),cx,cy):
                    if grid[nx][ny]==0:
                        grid[nx][ny]=1
                        que.append((nx,ny))
                    elif grid[nx][ny]==2:
                        return step
            step+=1
            
            
                        
    def setDest(self,grid,x,y):
        def dfs(grid,x,y):
            grid[x][y]=2
            
            for nx,ny in self.nextCoor(len(grid),x,y):
                if grid[nx][ny]==1:
                    dfs(grid,nx,ny)
        
        dfs(grid,x,y)
        
        

    def nextCoor(self,n,x,y):
        for nx,ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            yield (nx,ny)