class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i : [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count