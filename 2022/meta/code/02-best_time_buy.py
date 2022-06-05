def maxProfit(prices):
    min_price = 9999999
    max_profit = 0
    for pointer in range(len(prices)):
        min_price = min(min_price, prices[pointer])
        max_profit = max(max_profit, prices[pointer] - min_price)
    return max_profit


if __name__ == "__main__":
    print(maxProfit([7,6,4,3,1]))
