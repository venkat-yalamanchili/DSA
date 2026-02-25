def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index): # Go through V 378 and 379 for better understanding
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index  += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index
            
def quicksort(my_list, left, right):
    if left < right:  #because if left == right that means only 1 element not need to sort
        pivot_index = pivot(my_list , left, right)
        quicksort(my_list, left, pivot_index-1)
        quicksort(my_list, pivot_index+1, right)
    return my_list

print(quicksort([6,5,1,9,3,2,7,4,8],0,8))