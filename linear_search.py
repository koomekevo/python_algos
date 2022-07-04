def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return "Target is :" [i]
        else:
            return "Target not found"

def verify(index):
    numbers = [1,2,3,4,5,6,7,8,9]
    result = linear_search(numbers, 10)

    
