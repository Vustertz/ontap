def coinChange(coins, amount) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    n = len(coins)
    for i in range(1,amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i],1 + dp[i - c])
    if dp[amount] != amount + 1:
        return dp[amount]
    else:
        return -1
    
with open("input.txt") as f:
    lines = f.readlines()

with open('output.txt','w') as o:
    for i in range(0, len(lines), 2):
        coins = list(map(int, lines[i].split()))
        amount = int(lines[i+1])
        output = coinChange(coins,amount)
        o.write(str(output) + '\n')


