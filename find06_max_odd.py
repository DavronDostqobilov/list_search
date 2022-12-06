def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    i=0
    odd=[]
    while i<len(data):
        if data[i]%2==1:
            odd.append(data[i])
        i+=1
    j=0
    max1=odd[0]
    while j<len(odd):
        if max1<odd[j]:
            max1=odd[j]
        j+=1
    return max1
print(find_max_odd([2,3,7,5,78,5,9,3]))