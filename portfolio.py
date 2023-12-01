import csv

def loadInvestments(investmentFilename):
    investments = []
    with open(investmentFilename, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header
        next(csv_reader)  # Skip USA average row

        for row in csv_reader:
            # Grabs correct data and does estimated return math
            state = row[2]
            cost = float(row[4])
            returns_percentage = float(row[9])
            estimated_return = cost * returns_percentage
            investments.append((state, cost, estimated_return))

    return investments

def optimizeInvestments(investments, budget):
    # Initialize DP table
    dp_table = [[0 for i in range(budget + 1)] for i in range(len(investments) + 1)]
    # Track back keeps track of the of investments made
    traceback_table = [[[] for i in range(budget + 1)] for i in range(len(investments) + 1)]

    # Iterates over each investment and each possible budget amount
    for i in range(1, len(investments) + 1):
        for j in range(1, budget + 1):
            investment_cost = investments[i - 1][1]
            investment_return = investments[i - 1][2]

            if investment_cost <= j:
                # Choice to include the investment
                if dp_table[i - 1][j - int(investment_cost)] + investment_return > dp_table[i - 1][j]:
                    dp_table[i][j] = dp_table[i - 1][j - int(investment_cost)] + investment_return
                    # Updates name of the included investment
                    traceback_table[i][j] = traceback_table[i - 1][j - int(investment_cost)] + [investments[i - 1][0]]
                else:
                    # If not including investment is better it copies return value of previous row
                    dp_table[i][j] = dp_table[i - 1][j]
                    traceback_table[i][j] = traceback_table[i - 1][j]
            else:
                # If the cost of the current investment exceed budget, copies vlue from previous row
                dp_table[i][j] = dp_table[i - 1][j]
                traceback_table[i][j] = traceback_table[i - 1][j]

    # Traceback to find the selected investments
    selected_investments = traceback_table[len(investments)][budget]
    return dp_table[len(investments)][budget], selected_investments

investment_short = loadInvestments('zhvi-short.csv')
investment_full = loadInvestments('state_zhvi_summary_allhomes.csv')

# print(investment)

# print(optimizeInvestments(investment_short, 15))
print(optimizeInvestments(investment_full, 1500000))