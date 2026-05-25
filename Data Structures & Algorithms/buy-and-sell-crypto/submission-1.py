class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Bruteforce method:
        # profit = 0

        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         total = prices[j] - prices[i]

        #         profit = max(profit, total)

        # return profit

        #Optimal solution :

        profit = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                total = prices[right] - prices[left]
                profit = max(total, profit)

            else:
                left = right

            right += 1
        return profit