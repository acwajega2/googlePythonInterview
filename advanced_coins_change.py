##HOUSE KEEPING
# 1 qurter = 25 cents
# 1 dime = 10 cents
# 1 nickle = 5 cents
# 1 pennie = 1 cent 

def min_coins(cents):
    # if the cents r zero
    if cents < 1:
        return 0

    coins =[25,10,5,1]
    num_coins = 0
    for coin in coins:
        if cents >= coin:
            num_coins +=cents / coin
            cents = cents % coin
        
        if cents == 0:
            break
    return round(num_coins)

#print(min_coins(31))

# solution 2
def min_coin_2(cents):
    coins =[25,10,1]
    num_coins =[0]* len(coins)
    x = 0
    print(num_coins)
    used_coins = []
    for coin in coins:
        if cents > coin :
            used_coins.append(coin)
            x += cents / coin
            cents = cents % coin
        if cents == 0:
            break
    print(round(x))     
    print(used_coins)
    


min_coin_2(31)

