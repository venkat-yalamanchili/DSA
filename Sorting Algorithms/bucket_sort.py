import math

def bucketsort(customList):
    if not customList:
        return []
    
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    
    rangeVal = (maxValue - minValue) / numberofBuckets
    if rangeVal == 0: # if rangeVal is zero it means all the elements are same so just return the list
        return customList

    buckets = [[] for _ in range(numberofBuckets)]

    for j in customList:
        # FIX: If j is the maxValue, it will land in the last bucket 
        if j == maxValue:
            buckets[-1].append(j)
        else:                                               
            index_b = math.floor((j - minValue) / rangeVal) # this formula doesnt work for the max value in the list
            buckets[index_b].append(j)                      # here rangeVal will not be zero since above if condition

    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = insertionsort(buckets[i])
        sorted_array.extend(buckets[i])
    
    return sorted_array

def insertionsort(l: list):
    for i in range(1, len(l)):
        j = i
        while j > 0 and l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]
            j -= 1
    return l

print(bucketsort([6, 5, 1, 9, 3, 2, 7, 4, 8]))