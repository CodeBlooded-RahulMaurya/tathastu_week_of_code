def sort012( a, arr_size): 
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi: 
        if a[mid] == 0: 
            a[lo], a[mid] = a[mid], a[lo] 
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1: 
            mid = mid + 1
        else: 
            a[mid], a[hi] = a[hi], a[mid]  
            hi = hi - 1
    return a 
def printArray( a): 
    for k in a: 
        print (k)
l=int(input("Enter length of array to sort"))
arr =  []
print("Enter values in array one by one :")
for x in range(l):
    arr.append(int(input()))
arr_size = len(arr) 
print ("Array after sorting :\n")
printArray(arr)
arr = sort012( arr, arr_size) 