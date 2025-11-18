def pair_sum(myList, sum):
    new_lst = []
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i]+myList[j] == sum:
                new_lst.append(f"{myList[i]}+{myList[j]}")
    return new_lst