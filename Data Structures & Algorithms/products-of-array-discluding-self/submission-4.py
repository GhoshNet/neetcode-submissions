class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #Correct Solution:

        # n = len(nums)

        # result = [1] * n
        # prefix = 1

        # for i in range(n):
        #     result[i] = prefix
        #     prefix = prefix * nums[i]

        # postfix = 1
        # for i in range(n-1, -1, -1):
        #     result[i] *= postfix
        #     postfix *= nums[i]

        # return result

        #Revision:
        lenght = len(nums)
        result = [1] * lenght
        # print(result)
        prefix = 1
        postfix = 1
        for i in range(lenght):
            result[i] = prefix
            prefix *= nums[i]
        for i in range(lenght - 1, -1 , -1 ):
            result[i] *= postfix
            postfix *= nums[i]

        return result

            