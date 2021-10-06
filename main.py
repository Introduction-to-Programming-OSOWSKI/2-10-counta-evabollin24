def countA(w):
    count = 0
    for i in range(0, len(w)):
        if w[i] == "a":
            count = count + 1
        else:
            count = count
    return(count)