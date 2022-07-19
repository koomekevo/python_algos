def merge_sort(list):
    """
    Sorts a list in ascending order
    Return a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """
    
    if len(list) <= 1:
        return list