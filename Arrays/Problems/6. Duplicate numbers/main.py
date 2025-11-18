# My approach 

def remove_duplicates(arr):
    new_lst = []
    for i in arr:
        if i not in new_lst:  # this is also time consuming looking up an element in set is better
            new_lst.append(i)
    return new_lst

# lokking up element in set way better
# Better solution

def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst