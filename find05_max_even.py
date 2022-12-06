def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
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
        if max1<even[j]:
            max1=even[j]
        j+=1
    return max1
print(find_max_even([1,2,3,4,5,6,9,9,3]))
