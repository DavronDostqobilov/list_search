def find_max_min_sum(data):
    """
    Given the list of numbers, return the sum of the maximum and minimum numbers in the list
    args:
        data: list of numbers
    returns: sum of the maximum and minimum numbers in the list
    """
    i=0
    sum=data[0]
    while i<len(data):
        if sum<data[i]:
            sum=data[i]
        i+=1
    sum1=data[0]
    while i<len(data):
        if sum1>data[i]:
            sum1=data[i]
        i+=1
    return sum+sum1
print(find_max_min_sum([1,2,3,4,5]))
