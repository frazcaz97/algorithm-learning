import random
import time

arr = []
changeCount = 0

sizeOfList = input("enter size of list to sort: ")
for i in range(int(sizeOfList)):
        n = random.randint(0,1000)
        arr.append(n)
print("non-sorted list: " + str(arr))

def divide(array):
        global changeCount
        if len(array) > 1:
                mid = len(array)//2
                left = array[: mid]
                right = array[mid :]
                left = divide(left)
                right = divide(right)

                array = []

                while len(left) > 0 and len(right) > 0:
                        if left[0] < right[0]:
                                array.append(left[0])
                                left.pop(0)
                                changeCount += 1
                        else:
                                array.append(right[0])
                                right.pop(0)
                                changeCount += 1

                while len(left) > 0:
                        array.append(left[0])
                        left.pop(0)
                        changeCount += 1
                while len(right) > 0:
                        array.append(right[0])
                        right.pop(0)
                        changeCount += 1

        return array

startTime = int(round(time.time() * 1000))
print("sorted list: " + str(divide(arr)))
elapsedTime = int(round(time.time() * 1000)) - startTime
print("number of changes made to the list: " + str(changeCount))
print("time taken to sort the list: " + str(elapsedTime) + " milliseconds")
