def liner_search(l:list,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


print(liner_search([1,2,3,4,5,6], 6))