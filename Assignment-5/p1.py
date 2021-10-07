def max_profit(A):
    max_prices = []
    min_prices = []
    for i in range(1, len(A) - 1):
        if (A[i - 1] < A[i] and A[i] > A[i + 1]):
            if (len(min_prices) == 0):
                min_prices.append(A[0])
            max_prices.append(A[i])

        elif (A[i - 1] > A[i] and A[i] < A[i + 1]):
            min_prices.append(A[i])

        if (i == len(A) - 2 and A[i] < A[i + 1]):
            max_prices.append(A[i + 1])

    i = 1
    profit = 0
    for sp, cp in zip(max_prices, min_prices):
        print(f"{i}) S.P. - C.P. = {sp} - {cp} = {sp - cp}")
        profit += (sp - cp)
        i += 1

    return profit


prices = list(map(int, input("Enter the prices (seperated by space): ").split()))
print("Max Profit:", max_profit(prices))