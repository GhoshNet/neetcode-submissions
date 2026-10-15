class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = {}
        # for i, num in enumerate(nums):
        #     count[num] = count.get(num, 0) + 1

        # sorting = sorted(count.items(), key = lambda x: x[1], reverse = True)

        # result = []
        # for number, freq in sorting[:k]:
        #     result.append(number)
        # return result
        
        #Try 1 
        dic = {}
        for i, n in enumerate(nums):
            dic[n] = 1 + dic.get(n, 0)
            
        sorting = sorted(dic.items(), key = lambda x : x[1], reverse = True)
        # print(sorting)
        # Now sorting is a list of tuples, so we can slice the elements(tuples) of the list. 
        limit = sorting[:k]
        result = []
        for (number, freq) in limit:
            result.append(number)
        
        return result

        
