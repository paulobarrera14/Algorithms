import pandas as pd

prices_df = pd.read_csv('prices-split-adjusted.csv')
grouped_prices = prices_df.groupby('symbol')
securities = pd.read_csv('securities.csv')

def max_crossing_profit(prices, low, mid, high):
    left_sum = float('-inf')
    sum = 0
    buy_date = mid
    for i in range(mid, low - 1, -1):
        sum += prices[i]
        if sum > left_sum:
            left_sum = sum
            buy_date = i

    right_sum = float('-inf')
    sum = 0
    sell_date = mid + 1
    for i in range(mid + 1, high + 1):
        sum += prices[i]
        if sum > right_sum:
            right_sum = sum
            sell_date = i

    return left_sum + right_sum, buy_date, sell_date

def max_subarray(prices, low, high):
    if low == high:
        return prices[low], low, low
    else:
        mid = (low + high) // 2
        left_sum, left_low, left_high = max_subarray(prices, low, mid)
        right_sum, right_low, right_high = max_subarray(prices, mid + 1, high)
        cross_sum, cross_low, cross_high = max_crossing_profit(prices, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_sum, left_low, left_high
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_sum, right_low, right_high
        else:
            return cross_sum, cross_low, cross_high


max_profit = float('-inf')
best_stock = None
buy_date = None
sell_date = None

for symbol, group_data in grouped_prices:
    if group_data.empty:
        continue

    group_data = group_data.sort_values(by='date')

    # Calculate day-to-day price changes
    daily_changes = group_data['close'].diff().fillna(0).tolist()

    profit, buy, sell = max_subarray(daily_changes, 0, len(daily_changes) - 1)
    if profit > max_profit:
        max_profit = profit
        best_stock = symbol
        buy_date = group_data.iloc[buy]['date']
        sell_date = group_data.iloc[sell]['date']

matching_security = securities[securities['Ticker symbol'] == best_stock]

if matching_security.empty:
    print(f"Could not find security information for {best_stock}.")
else:
    company_name = matching_security['Security'].values[0]
    print(f'Best stock to buy: "{company_name}" on {buy_date} and sell on {sell_date} with profit of {max_profit}')
