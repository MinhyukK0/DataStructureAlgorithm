class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for node, node_next, time in times:
            graph[node].append((node_next, time))
           
        Q = [(0, k)]
        dist = collections.defaultdict(int)
        
        while Q:
            time, node_ = heapq.heappop(Q)
            if node_ not in dist:
                dist[node_] = time
                for node__, t in graph[node_]:
                    new_t = time + t
                    heapq.heappush(Q, (new_t, node__))
                    
        if len(dist) == n:
            return max(dist.values())
        
        return -1