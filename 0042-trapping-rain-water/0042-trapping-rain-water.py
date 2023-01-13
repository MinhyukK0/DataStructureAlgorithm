class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height)<3:
            return 0
        left, right = 0, len(height)-1
        l_max, r_max = height[left], height[right]
        vol = 0
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max < r_max:
                vol += l_max - height[left]
                left += 1
            else:
                vol += r_max - height[right]
                right -= 1
        return vol