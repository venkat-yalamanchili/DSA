def insertionsort(l:list):
    for i in range(1, len(l)):
        j = i
        while l[j-1] > l[j] and j >0:
            l[j-1], l[j] = l[j], l[j-1]
            j -=1 
    print(l)

insertionsort([6,5,1,9,3,2,7,4,8])