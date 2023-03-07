def make_readable(seconds):

    # take non negative input of seconds
    # convert into HH:MM:SS
    # HH max 99, MM/SS max 59
    # start with hours - in input is larger than 3600 return integer and save remainder

    hours = divmod(seconds, 3600)
    minutes = divmod(hours[1], 60)
    sec = divmod(minutes[1], 1)

    answer = str(hours[0]).zfill(2) + ":" + str(minutes[0]).zfill(2) + ":" + str(sec[0]).zfill(2) 
    
    return answer