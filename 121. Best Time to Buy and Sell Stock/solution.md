## LeetCode 121. Best Time to Buy and Sell Stock

### Solution:
1. Create two variables to represent the profit and the buying price.
2. Loop over the list of prices, with the variable representing the selling price.
3. If the selling price is higher than the buying price, calculate the profit and update the maximum profit.
4. If the selling price is lower than the buying price, update the buying price to the current price in the loop.