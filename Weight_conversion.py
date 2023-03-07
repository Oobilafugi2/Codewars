import re

def order_weight(strng):

    # weight will come in as string
    # convert string to int
    # add each digit of weight
    # order them by smallest to largest sum

    strng2 = re.sub(' +', ' ', strng)
    strng_list = strng2.strip().split()

    new_list = []

    numbers = 0

    for i in strng_list:
        
        numbers = 0
        
        for digit in i:
            numbers += int(digit)
        
        new_list.append(numbers)

    res = sorted([(new_list[i], strng_list[i]) for i in range(0, len(strng_list))])
    final = ' '.join([x[1] for x in res])
    
    return final