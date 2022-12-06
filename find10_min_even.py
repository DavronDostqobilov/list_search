def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    i=0
    even=[]
    while i<len(data):
        if data[i]%2==0:
            even.append(data[i])
        i+=1
    j=0
    max1=even[0]
    while j<len(even):
        if max1>even[j]:
            max1=even[j]
        j+=1
    return max1
print(find_min_even([1,7,9,90,789,6,4,32,12,1]))

