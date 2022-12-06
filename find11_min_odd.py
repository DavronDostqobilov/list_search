def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    i=0
    even=[]
    while i<len(data):
        if data[i]%2==1:
            even.append(data[i])
        i+=1
    j=0
    mn1=even[0]
    while j<len(even):
        if mn1>even[j]:
            mn1=even[j]
        j+=1
    return mn1
print(find_min_odd([1,32,4,5,6,8,90,0,]))

