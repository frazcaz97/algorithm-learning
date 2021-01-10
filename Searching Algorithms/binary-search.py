import math

def binarySearch(arr, target):
    l = 0
    r = len(arr) - 1
    print ("left: " + str(l), " right: " + str(r))

    while l <= r:
        m = math.floor((l + r) / 2)
        print ("middle: " + str(m)
        )
        if (arr[m] < target):
            l = m + 1
            print (str(arr[m]) + " is less than " + str(target))
        elif (arr[m] > target):
            r = m - 1
            print (str(arr[m]) + " is greater than " + str(target))
        else:
            print (str(arr[m]) + " is equal to " + str(target))
            return m
    print (str(target) + " not found in array")
    return "not found"
        

index = binarySearch(["a", "b", "c", "d", "e", "f", "g"], "a")
print ("found target at index: " + str(index))