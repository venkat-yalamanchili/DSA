# this is greedy approach there is another with dynamic programming
def coin_change(amount,coins):
    coins.sort(reverse = True)

    count = 0
    result = []

    for coin in coins:
        if amount>= coin:
            num_coins = amount // coin
            count += num_coins
            amount -= num_coins*coin

            result.extend([coin]*num_coins)
    # If amount is not 0, it means we couldn't make exact change
    if amount >0 :
        return -1,[]
    
    return count, result

available_coins = [1, 5, 10, 25]
target = 63

total_count, used_coins = coin_change(target, available_coins)

print(total_count, used_coins)