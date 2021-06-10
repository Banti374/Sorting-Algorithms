
def insertionSort():

    arr = []
    r = int(input("Enter the length of the array : "))
    i = 1
    while i <= r:
        x = int(input("Enter the value : "))
        i += 1
        arr.append(x)
    print(arr)

    n = len(arr)

    for i in range(1,n):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i])



insertionSort()
