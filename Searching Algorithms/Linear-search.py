arr = ["a", "b", "c", "d", "e"]
print(arr)
word = input("word to search for?")

for i, value in enumerate(arr, start=0):
    print(i)
    if value == word:
        print("we have found your word at index: " + str(i))
        break
    elif i == len(arr) - 1:
        print("word not in list, sorry")
