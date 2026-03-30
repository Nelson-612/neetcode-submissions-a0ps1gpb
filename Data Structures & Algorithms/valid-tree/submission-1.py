class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = [[] for i in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)


        visited = set()
        queue = deque([(0, -1)])
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                visited.add(neighbor)
                queue.append((neighbor, node))
        
        if len(visited) == n:
            return True
        else:
            return False
