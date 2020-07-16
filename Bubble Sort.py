import random
import time

def bubbleSort():
    arr = []
    changeCount = 0
    sizeOfList = input("enter size of list to sort: ")
    for i in range(int(sizeOfList)):
        n = random.randint(0,1000)
        arr.append(n)

    print("generated list: " + str(arr))
    startTime = int(round(time.time() * 1000))
    for j in range(len(arr)-1):
        for k in range(len(arr)-1):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
                changeCount += 1
    elapsedTime = int(round(time.time() * 1000)) - startTime
    print("sorted list: " + str(arr))
    print ("with " + str(changeCount) + " changes to the list")
    print ("and took " + str(elapsedTime) + " miliseconds to sort") 

bubbleSort()
