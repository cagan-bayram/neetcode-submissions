class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i == j:
                    continue
                areas.append(min(heights[i], heights[j]) * abs(i-j))
        
        return max(areas)