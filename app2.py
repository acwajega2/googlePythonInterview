#### MAKING A CHANGE APP

#----GET THE NUMBER OF COINS GIVEN CHANGE AS 31 CENTS
#---- 1 quarter ==>>>>>>(25 cents)
#---- 1 nickel ==>>>>>>(5 cents)
#-----1 pennies ==>>>>>(1 cent)
#------1 dime ==>>>>>(10 cents)

#EXAMPLE--GIVEN 31 cents-----you give back 3 coins in (1 quarter, 1 nickel and i pennies)


def min_num_coins(cents):
    if cents < 1 :
        return 0
    coins = [25,10,5,1]


    #----in order to get the minum number of coins, we use the maximum number of coins as much as possible
    #  but for the maximum number of coins, we choose the one that has a lesser remainder
    rem_num =0
    num_coins =0
    coin_selected = 0
    new_cents = cents
    for coin in coins:
        rem_num = cents % coin
        if rem_num < 3:
            while  new_cents >= coin :
               new_cents = new_cents - coin
               num_coins +=1

    return num_coins
        




print(min_num_coins(31))