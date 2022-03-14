class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(ele, start: int, k: int):
            if k == 0:
                res.append(ele[:])
                return

            for i in range(start, n + 1):
                ele.append(i)
                dfs(ele, i + 1, k - 1)
                ele.pop()

        dfs([], 1, k)

        return res