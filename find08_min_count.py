def find_min_count(data):
    """
    Given the list of numbers, Find count of minimum numbers in the list
    args:
        data: list of numbers
    returns: count of minimum numbers in the list
    """
    i=0
    mn=data[0]
    while i<len(data):
        if mn>data[i]:
            mn=data[i]
        i+=1
    return data.count(mn)
print(find_min_count([1,3,4,6,8,-32,-2,-32]))
