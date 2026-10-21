class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        lenght = len(nums)
        result = [1] * lenght
        for i in range(lenght):
            result[i] *= prefix
            prefix *= nums[i]
        for j in range(lenght - 1, -1, -1):
            result[j] *= postfix
            postfix *= nums[j]
        return result