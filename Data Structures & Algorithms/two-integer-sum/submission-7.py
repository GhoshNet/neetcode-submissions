class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #Initialise a Dictionary to store num and it's index
        # lookupTable = {}
        # #Enumerate helps us use the index along with number in the list
        # for index, num in enumerate(nums):
        #     #Iterate through every number
        #     diff = target - num
        #     if diff in lookupTable:
        #         #We have to return lower index 1st. 
        #         #Following condition is optional. Think about it. 
        #         if index < lookupTable[diff]:
        #             return [index, lookupTable[diff]]
        #         else:
        #             return [lookupTable[diff], index]

        #     #Store Key-Value pair in the dict for next iteration if diff not found
        #     lookupTable[num] = index

        lookupTable = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookupTable:
                # print ([lookupTable[diff], i])
                return [lookupTable[diff], i]
            lookupTable[num] = i

