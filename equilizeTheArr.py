def equilizeTheArr(arr):
    return min([ len(arr)-arr.count(i) for i in set(arr) ])
