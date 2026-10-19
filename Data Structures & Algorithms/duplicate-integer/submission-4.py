class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #No look trials:

        # # Solution 1
        # if len(set(nums)) != len(nums):
        #     return True
        # else:
        #     return False

        #Solution 2:
        count = {}
        for num in nums:
            if count.get(num):
                return True
            count[num] = 1
        return False