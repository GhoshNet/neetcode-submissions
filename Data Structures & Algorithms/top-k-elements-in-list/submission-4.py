class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {        }
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # print(count)
        sorting = sorted(count.items(), key = lambda x : x[1], reverse = True)
        # print(type(sorting))
        topk = sorting[:k]
        # print(topk)
        result = []
        for num, freq in topk:
            result.append(num)
        return result
        