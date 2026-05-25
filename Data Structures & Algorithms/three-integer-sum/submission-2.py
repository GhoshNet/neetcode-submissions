class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        ans = 0
        if len(nums) < 3:
            return result
        elif len(nums) == 3:
            for i, n in enumerate(nums):
                ans += n
            if ans == 0:
                return [nums]
            else:
                return result
        else:
            
            array = sorted(nums)
            for i in range(len(array)):
                if i > 0 and array[i] - array[i-1] == 0:
                    continue

                left = i + 1 #Taking the next value after "i" to avoid duplication and to maintain continuity
                right = len(array) - 1

                while left < right:

                    if (array[i] + array[left] +array[right] > 0):
                        right -=1
                    elif (array[i] + array[left] +array[right] < 0):
                        left +=1
                    elif (array[i] + array[left] +array[right] == 0):
                        result.append([array[i], array[left], array[right]])
                        left += 1

                        #Skip duplicates until a fresh left value is found. Keep in mind that "i" is still the same if you are confused.
                        while left < right and array[left] == array[left - 1]: #This is checking the left's value is same for which we just operated.
                            left += 1
            return result