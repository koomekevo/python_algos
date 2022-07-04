def binary_search(list, target):
    first = 0
    last = len(list) - 1
    midpoint = first + last // 2
    
    while (first <= last):
        if list[midpoint] == target:
            print("Target is : ", target)
        elif list[midpoint] < target:
            midpoint + 1 // 2
        else: 
            list[midpoint] > target
            midpoint - 1 // 2