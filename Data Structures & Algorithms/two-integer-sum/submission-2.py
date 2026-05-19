class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookupTable = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookupTable:
                if i < lookupTable[diff]:
                    return [i,lookupTable[diff]]
                else:
                    return [lookupTable[diff], i]
            lookupTable[num] = i
