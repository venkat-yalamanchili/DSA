def missing_number(arr, n):
    total = (n*(n+1))/ 2
    sum_arr = sum(arr)
    missing = total-sum_arr
    return missing


print(missing_number([1, 2, 3, 4, 5, 6, 7, 9], 9))