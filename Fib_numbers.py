def productFib(prod):

    # take list of fibonnaci numbers
    # input a number to check
    # that number needs to have two consecutive fibonacci numbers that when multiplied together equal the input

    # create fibonacci list
    fib = [0, 1]
    multiples = []

    for n in range(2, 200):
        fib.append(fib[n-1] + fib[n-2])

    # compare inputted number to multiples in list
    for x in range(len(fib)):

        #create new list of multiples to compare against
        multiples.append(fib[x] * (fib[x + 1]))

        # compare mutliple sets against prod to see if they match
        if prod == (fib[x] * (fib[x + 1])):
            return [fib[x], (fib[x + 1]), True]
            
        elif prod < (fib[x] * (fib[x + 1])):
            return [fib[x], (fib[x + 1]), False] 