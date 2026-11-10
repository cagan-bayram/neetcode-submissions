class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for num in nums:
            numsWithoutNum = nums.copy()
            numsWithoutNum.remove(num)
            product = 1
            for no in numsWithoutNum:
                product *= no
            products.append(product)
        return products
