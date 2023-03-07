from itertools import combinations

def choose_best_sum(t, k, ls):

    # t is the upper limit of miles
    # k is the number of towns
    # ls is the list of the distances between towns

    # return the sum of the list of k number of towns that gets closest to T

    # add up all combinations of distances with k number of items
    
    combo = list(combinations(ls, k))
    sums = sorted([sum((x[0:k])) for x in combo])
    
    print(t, k, ls)
    
    for i in range(0, len(sums)):
        if sums[i] > t and sums[i-1] <= t:
            return sums[i-1]
        if sums[len(sums) - 1] <= t:
            return sums[len(sums) - 1]