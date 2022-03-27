class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for node, next_node, time in times:
            graph[node].append((next_node, time))
            
        Q = [(0,k)]
        dist = collections.defaultdict(int)
        
        while Q:
            time, cur = heapq.heappop(Q)
            if cur not in dist:
                dist[cur] = time
                for dist_node, dist_time in graph[cur]:
                    total_t = dist_time + time
                    heapq.heappush(Q, (total_t, dist_node))
                    
        if len(dist) == n:
            return max(dist.values())
        
        return -1