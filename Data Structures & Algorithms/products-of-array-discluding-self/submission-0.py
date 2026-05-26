class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #The below division method fails when input has zeroes

        # l = len(nums)
        # mult = 1
        
        # result = []
        # for i in nums:
            
        #     mult = (mult*(i))
        # j = 0
        # while j < l:
        #     if nums[j] == 0:
        #         result.append(0)
        #     else:
        #         result.append(int(mult//nums[j]))
        #     j += 1
        # return result

        #Correct Solution:

        n = len(nums)

        result = [1] * n
        prefix = 1

        for i in range(n):
            result[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(n-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
            