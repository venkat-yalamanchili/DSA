def selectionsort(l:list):
    for i in range(len(l)):
        min_index = i
        for j in range(i+1,len(l)):
            if l[min_index] > l[j]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    print(l)

selectionsort([6,5,1,9,3,2,7,4,8])