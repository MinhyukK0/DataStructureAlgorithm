class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # set up graph
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        traced = set()
        visited = set()

        # set func
        def dfs(a):
            # if recur structure return False
            if a in traced:
                return False
            # if visited node return True
            if a in visited:
                return True
            # start search graph
            traced.add(a)
            for b in graph[a]:
                if not dfs(b):
                    return False
            traced.remove(a)
            # add visited node
            visited.add(a)
            return True
        # run dfs
        for x in list(graph):
            if not dfs(x):
                return False
        return True
