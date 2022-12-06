def find_max_count(data):
    """
    Given the list of numbers, Find count of maximum numbers in the list
    args:
        data: list of numbers
    returns: count of maximum numbers in the list
    """
    i=0
    sum=data[0]
    while i<len(data):
        if sum<data[i]:
            sum=data[i]
        i+=1
    return data.count(sum)
print(find_max_count([4,9,5,2,5,7,9]))
