class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    #     if nums == []:
    #         return 0
        
    #     sorting = sorted(nums)
    #     result = 1
    #     current = 1
    #     i=0
    #     while i <= len(nums):
    #     # for i in range(len(nums)):
    #         if (i+1) >= len(nums):
    #             return result
    #         elif sorting[i] == sorting[i+1]:
    #             i +=1
    #             continue
    #         elif sorting[i] == sorting[i+1] - 1:
    #             current += 1
    #         else:
    #             current = 1
    #         if current > result :
    #             result = current
    #         i += 1

    #     return result

    # #The above solution is correct but the time complexity is O(nlogn).
    # #We need O(n), so use hashmaps as below:

        if nums == []:
            return 0
        longest = 1 
        hashmap = set(nums)
        for num in hashmap:
            if (num - 1) not in hashmap:
                chain = 1
                while num+chain in hashmap:
                    chain += 1

                longest = max(longest, chain)
        
        return longest