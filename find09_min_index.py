def find_min_index(data):
    """
    Given the list of numbers, return the index of minimum number in the list
    args:
        data: list of numbers
    returns: index of minimum number in the list
    """
    i=0
    mn=data[0]
    while i<len(data):
        if mn>data[i]:
            mn=data[i]
        i+=1
    return data.index(mn)
print(find_min_index([1,3,4,6,8,-32,-2]))

