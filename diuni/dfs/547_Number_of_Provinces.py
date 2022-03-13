class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        
        
        def dfs(idx, connections, visited):
            # print("i:", idx, isVisited)
            visited[idx] = True
            for i, con in enumerate(connections):
                if con == 1 and visited[i] == False:
                    dfs(i, isConnected[i], visited)
            return visited
        
        province = 1
        visited = [False] * len(isConnected)
        start = 0
        
        while True:
            visited = dfs(start, isConnected[start], visited)
            if False in visited:
                start = visited.index(False)
                province += 1
            else:
                break
        
        return province