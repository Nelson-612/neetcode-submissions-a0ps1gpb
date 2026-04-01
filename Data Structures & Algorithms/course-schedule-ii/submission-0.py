class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        if not prerequisites:
            return list(range(numCourses))

        adj = { i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        visited = set()
        completed = set()
        order = []

        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True

            visited.add(course)

            for prereq in adj[course]:
                if not dfs(prereq):
                    return False

            visited.remove(course)
            completed.add(course)
            order.append(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order