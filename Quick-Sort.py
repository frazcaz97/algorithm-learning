import random
import time

arr = []
changeCount = 0

sizeOfList = input("enter size of list to sort: ")
for i in range(int(sizeOfList)): #create array of random numbers
        n = random.randint(0,1000)
        arr.append(n)
print("non-sorted list: " + str(arr))

def quickSort(arr,low,high):
        if low < high:
                pivot = partition(arr, low, high)   #returns the number to divide our array by
                quickSort(arr, low, pivot-1)    #sort first half of array
                quickSort(arr, pivot+1, high)   #sort second half of array

        return arr

def partition(arr, low, high):
        global changeCount
        pivot = arr[high]   #pivot array by last index of this array sort
        i = low-1
        j = low

        while j <= high-1:

                if arr[j] < pivot:   #swap the array elements
                        i+=1
                        a = arr[i]
                        b = arr[j]
                        arr[i] = b
                        arr[j] = a
                        changeCount += 1
                j+=1

        #swap these indexes to put them in the correct place
        c = arr[i+1]
        d = arr[high]
        arr[i+1] = d
        arr[high] = c
        changeCount += 1

        return i+1
startTime = int(round(time.time() * 1000))
elapsedTime = int(round(time.time() * 1000)) - startTime
print("sorted list: " + str(quickSort(arr, 0 , len(arr)-1)))
print("number of changes made to the list: " + str(changeCount))
print("time taken to sort the list: " + str(elapsedTime) + " milliseconds")