class Solution:
    def trap(self, height: List[int]) -> int:
        # solution 1: pointer
        # if not height or len(height)<3:
        #     return 0
        # left, right = 0, len(height)-1
        # l_max, r_max = height[left], height[right]
        # vol = 0
        # while left < right:
        #     l_max = max(l_max, height[left])
        #     r_max = max(r_max, height[right])
        #     if l_max < r_max:
        #         vol += l_max - height[left]
        #         left += 1
        #     else:
        #         vol += r_max - height[right]
        #         right -= 1
        # return vol
        
        # solution 2: stack
        stack = []
        vol = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                width = i - stack[-1] -1
                h = min(height[i], height[stack[-1]]) - height[top]
                vol += width * h
            stack.append(i)
        
        return vol