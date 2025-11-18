
def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for i in lst:
            counter[i] = counter.get(i,0) + 1 
        return counter
    return count_elements(list1) == count_elements(list2)