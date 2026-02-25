def merge_sort(arr):
    if len(arr) <= 1:  # Base case:if the list is 1 or 0 elements, it's already sorted
        return arr

    mid = len(arr) // 2  #DIVIDE: Find the midpoint and split the array
    left = merge_sort(arr[:mid])   # Recursive call for the left half
    right = merge_sort(arr[mid:])  # Recursive call for the right half

    
    result = [] # CONQUER (Merge): Combine the sorted halves
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:]) # Append any remaining elements
    result.extend(right[j:])
    return result

numbers = [64, -12, 25, -12, 22, 90, 22, 0, -3]
print(merge_sort(numbers))