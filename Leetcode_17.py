class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                res.append(path)
                return
            for idx in range(index, len(digits)):
                for char in my_dict[digits[idx]]:
                    dfs(idx + 1, path + char)

        my_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []
        if not digits:
            return res
        dfs(0, "")

        return res