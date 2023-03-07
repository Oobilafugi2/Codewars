from collections import defaultdict

def scramble(s1, s2):

    chars = defaultdict(int)
    chars2 = defaultdict(int)

    for x in s1:
        chars[x] += 1
    for y in s2:
        chars2[y] += 1
    
    counter = 0

    
    for i in range(len(s2)):
        if chars2[s2[i]] > chars[s2[i]]:
            counter += 1
        else:
            counter += 0
    
    if counter >= 1:
        return False
    else:
        return True