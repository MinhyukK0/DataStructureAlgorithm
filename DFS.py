graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def recur_dfs(v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = recur_dfs(w, discovered)
    return discovered

print(recur_dfs(1))

def iter_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

print(iter_dfs(1))