class Item:
    def __init__(self,value,weight):
        self.value = value
        self.weight = weight
        self.ratio = value/weight

def knapsack(capacity,items):
    items.sort(key=lambda x:x.ratio, reverse = True)

    total_value = 0
    for item in items:
        if capacity == 0:
            break

        if capacity>= item.weight:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += item.value *(capacity/item.weight)
            capacity = 0

    return total_value

item_list = [Item(60, 10), Item(100, 20), Item(120, 30)]
print(knapsack(50,item_list))