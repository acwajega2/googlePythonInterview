a =[1,2,3,4,5,6,7,8,9,10]
b =[4,5,6]

# print from position one upto but not including the last postion
print(a[1:3])

# printing from the first postion upto the  forth position
print(a[:4])

#printing from the forth position to the end not including the forth position
print(a[4:])

#LIST METHODS
# append--adds items
# count -- find number of items
# extend -- ends items at the end of the list
# index --search items at the index position
# insert --alows the list to be expanded in the list
# pop --pulls things from the top of the list
# remove --- removes an item in the middle
# reverse -- flips the order of the list
#sort --sorts the order of the list.




### USING THE LIST SPLIT FUNCTION

test ='this is wajega allan christopher'
def find_surname(word,search_word):
    word_list = word.split()
    if search_word in word_list :
        return True
    else :
        return False
    

if find_surname(test,'wajega') :
    print('Found Name')
else :
    print('Sorry, nothing was found!!!')

def get_email_id_and_company(email):
    email_id = email.split('@')
    company = email_id[1].split('.')
    result ={
        'email_id':email_id [0],
        'company':company[0]
    }

    return result
print(get_email_id_and_company('acwajega@gmail.com'))