def dirReduc(arr):

    # given list of cardinal directions
    # remove immediate pairs
    # get route with no backtracking
    resume = True

    while resume:
        resume = False
        for i in range(1, len(arr)):
            
            
            if arr[i] == "NORTH" and arr[i-1] == "SOUTH":
                del arr[i]
                del arr[i-1]
                resume = True
                break
            
            if arr[i] == "SOUTH" and arr[i-1] == "NORTH":
                del arr[i]
                del arr[i-1]
                resume = True
                break

            if arr[i] == "EAST" and arr[i-1] == "WEST":
                del arr[i]
                del arr[i-1]
                resume = True
                break

            if arr[i] == "WEST" and arr[i-1] == "EAST":
                del arr[i]
                del arr[i-1]
                resume = True
                break
            

    return arr