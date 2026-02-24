def bubblesort(l:list) -> None:
    for i in range (len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j] , l[j+1] = l[j+1] , l[j]
    print(l)


bubblesort([6,5,1,9,3,2,7,4,8])