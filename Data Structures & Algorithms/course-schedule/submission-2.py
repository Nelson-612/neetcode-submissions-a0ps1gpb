class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        preCourse = set()
        visited = set()

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        def dfs(course):
            if course in visited:
                return True
            if course in preCourse:
                return False

            preCourse.add(course)
            for i in adj[course]:
                if dfs(i) == False:
                    return False
            preCourse.remove(course)
            visited.add(course)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True