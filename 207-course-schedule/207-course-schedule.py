class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # set up graph
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
         
        traced = set()
        visited = set()
        
        def dfs(a):
            if a in traced:
                return False
            if a in visited:
                return True
            traced.add(a)
            for i in graph[a]:
                if not dfs(i):
                    return False
            traced.remove(a)
            visited.add(a)
            return True
        for a in list(graph):
            if not dfs(a):
                return False
        return True