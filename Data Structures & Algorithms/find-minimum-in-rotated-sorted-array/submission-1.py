class Solution:
    def findMin(self, nums: List[int]) -> int:
        # BINARY SEARCH METHOD
        first = 0
        last = len(nums) - 1
        res = nums[0]
        while first <= last:
            if nums[first] < nums[last]:
                res = min(res, nums[first])
                break
            mid = first + (last - first) // 2
            res = min(res, nums[mid])    
            if nums[mid] >= nums[first]:
                first = mid + 1
            else:
                last = mid - 1
        return res
            
