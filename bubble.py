

def bubbleSort():
    arr = []
    r = int(input("Enter the length of the array : "))
    i = 1
    while i <= r:
        x = int(input("Enter the value : "))
        i += 1
        arr.append(x)
    print(arr)

    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print("Sorted array is:")
    for i in range(len(arr)):
        print("%d" % arr[i]),


bubbleSort()

