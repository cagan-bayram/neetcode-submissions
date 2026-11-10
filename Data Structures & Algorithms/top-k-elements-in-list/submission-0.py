class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurs = [nums.count(i) for i in nums]
        numsAndoccurs = {k:v for (k,v) in zip(nums, occurs)}
        numsAndoccurs = sorted(numsAndoccurs.items(), key=lambda x: x[1])
        numsNew = list(reversed(numsAndoccurs))
    
        out = []
        for m in range(k):
            out.append(numsNew[m][0])

        return out