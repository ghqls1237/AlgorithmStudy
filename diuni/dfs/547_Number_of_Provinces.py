class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        # 2022-03-13

        # First Trial 

        # Time Complexity: O(n)??? /   Runtime: faster than 49.33%
        # Space Complexity: O(n) /   Memory Usage: less than 13.89% 
        
        def dfs(idx, connections, visited):
        # def dfs(idx, isConnected, visited):
            visited[idx] = True
            for i, con in enumerate(connections):
            # for i, con in enumerate(isConnected[idx]):
                if con == 1 and visited[i] == False:
                    dfs(i, isConnected[i], visited)
                    # dfs(i, isConnected, visited)
            return visited
        
        province = 1
        visited = [False] * len(isConnected)
        start = 0

        
        while True:
            visited = dfs(start, isConnected[start], visited)
            # visited = dfs(start, isConnected, visited)
            if False in visited:
                start = visited.index(False)
                province += 1
            else:
                break
        
        return province