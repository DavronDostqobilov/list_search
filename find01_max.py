def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    i=0
    sum=data[0]
    while i<len(data):
        if sum<data[i]:
            sum=data[i]
        i+=1
    return sum
print(find_max([4,5,2,5,7,9]))
    