class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i, num in enumerate(nums):
            count[num] = count.get(num, 0) + 1

        sorting = sorted(count.items(), key = lambda x: x[1], reverse = True)

        result = []
        for number, freq in sorting[:k]:
            result.append(number)
        return result
        


            