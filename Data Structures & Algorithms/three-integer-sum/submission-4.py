class Solution:
    def threeSum(self, nums: List[int]) -> List[int]:
        triplets = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[j] + nums[i] + nums[k] == 0:
                        triplets.append([nums[i],nums[j],nums[k]])

        threes = []
        for lst in triplets:
            threes.append(sorted(lst))
    
        threes = list(set(tuple(x) for x in threes))
        return threes
                