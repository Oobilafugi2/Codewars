def last_digit(n1, n2):

    # get n1 ** n2 (n1 raised to the power of n2)
    # return last digit ([-1])
    # find answer, convert to string

    n1last = int(repr(n1)[-1])

    two = [2, 4, 8, 6]
    three = [3, 9, 7, 1]
    four = [4, 6]
    seven = [7, 9, 3, 1]
    eight = [8, 4, 2, 6] 
    nine = [9, 1]

    if n2 == 0:
        return 1
    
    if n1last in [0, 1, 5, 6]:
        return n1last
    
    if n1last == 2:
        number = n2 % 4
        return two[number - 1]
    
    if n1last == 3:
        number = n2 % 4
        return three[number - 1]

    if n1last == 4:
        number = n2 % 2
        return four[number - 1]

    if n1last == 7:
        number = n2 % 4
        return seven[number - 1]
    
    if n1last == 8:
        number = n2 % 4
        return eight[number - 1]

    if n1last == 9:
        number = n2 % 2
        return nine[number - 1]