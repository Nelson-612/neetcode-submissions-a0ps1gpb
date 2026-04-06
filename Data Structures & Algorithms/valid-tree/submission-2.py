class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = [[] for i in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)


        visited = set()
        
        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
        
            return True

        dfs(0, -1)
        return len(visited) == n
