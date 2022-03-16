class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        res = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            res.append(a)
        dfs("JFK")
        return res[::-1]