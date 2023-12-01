from time import time

#Lab 7 Dynamic programing

# Below are two algorithms (DAC and DP) to compute the
# minimum number of coins required to produce A cents worth of change
# The DP version also prints out the coins needed to produce this min

# Algorithm 1: Divide-and-Conquer
def DACcoins(coins, amount):
    if amount == 0: # The base case
        return 0
    else: # The recursive case
        minCoins = float("inf")
        for currentCoin in coins: # Check all coins
            # If we can give change
            if (amount - currentCoin) >= 0:
                # Calculate the optimal for currentCoin
                currentMin = DACcoins(coins, amount-currentCoin) + 1
                # Keep the best
                minCoins = min(minCoins, currentMin)
        return minCoins

# Algorithm 2: Dynamic Programming with Traceback
def DPcoins(coins, amount):
    # Create the initial tables, the amount it is multiplies by is a placeholder, so it could be any number
    coin_table = [amount + 1] * (amount + 1)
    # Fill in the base case(s)
    coin_table[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            coin_table[x] = min([coin_table[x], coin_table[x - coin] + 1])
    # Check if solution exists and fill rest of table
    if coin_table[amount] == amount + 1:
        return -1 # Return optional number of coins
    # Perform the traceback to print result
    current_amount = amount
    coins_used = []
    while current_amount > 0:
        for coin in coins:
            # Ex for amount = 29, coin_table[29 - 5] -> coin_table[24] = 2, coin_table[29] = 3, 3 - 1 = 2 so this condition tells us 5 is a coin in this optimized outcome since
            # from coin_table[24] you know it can be solved with 2 coins, making the total number of coins 3
            if current_amount - coin >= 0 and coin_table[current_amount - coin] == coin_table[current_amount] - 1:
                coins_used.append(coin)
                current_amount -= coin
                break

    return coin_table[amount], coins_used

C = [1,5,10,12,25] # Coin denominations (must include a penny)
A = int(input('Enter desired amount of change: '))
assert A>=0
print("DAC:")
t1 = time()
numCoins = DACcoins(C,A)
t2 = time()
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")
print("DP:")
t1 = time()
numCoins, coins_used = DPcoins(C,A)
t2 = time()
for coin in coins_used:
    print(coin)
print("optimal:",numCoins," in time: ",round((t2-t1)*1000,1),"ms")