class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Implementing Python Sets because sets don't store duplicate values 
        s = set(nums)
        if len(s) == len(nums):
            return False
        else:
            return True