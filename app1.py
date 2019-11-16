#### MAKING A CHANGE APP

#----GET THE NUMBER OF COINS GIVEN CHANGE AS 31 CENTS
#---- 1 quarter ==>>>>>>(25 cents)
#---- 1 nickel ==>>>>>>(5 cents)
#-----1 pennies ==>>>>>(1 cent)
#------1 dime ==>>>>>(10 cents)

#EXAMPLE--GIVEN 31 cents-----you give back 3 coins in (1 quarter, 1 nickel and i pennies)

def num_coins(cents):
   coins =[25,10,5,1]
   num_coins = 0
   coins.sort(reverse=True)
   new_cents = cents
   for coin in coins:
       while  new_cents >= coin :
           new_cents = new_cents - coin
           num_coins +=1
   print(str(num_coins))

          
num_coins(31)
