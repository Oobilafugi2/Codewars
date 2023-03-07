def zero(operator = None):
    if operator == None:
        return 0
    else:
        return operator(0) 
def one(operator = None):
    if operator == None:
        return 1
    else:
        return operator(1) 
def two(operator = None):
    if operator == None:
        return 2
    else:
        return operator(2) 
def three(operator = None):
    if operator == None:
        return 3
    else:
        return operator(3) 
def four(operator = None):
    if operator == None:
        return 4
    else:
        return operator(4) 
def five(operator = None):
    if operator == None:
        return 5
    else:
        return operator(5) 
def six(operator = None):
    if operator == None:
        return 6
    else:
        return operator(6) 
def seven(operator = None):
    if operator == None:
        return 7
    else:
        return operator(7) 
def eight(operator = None):
    if operator == None:
        return 8
    else:
        return operator(8) 
def nine(operator = None):
    if operator == None:
        return 9
    else:
        return operator(9) 

def plus(number):
    return lambda y: y + number
    
def minus(number):
    return lambda y: y - number 

def times(number):
    return lambda y: y * number 

def divided_by(number): 
    return lambda y: int(y / number)