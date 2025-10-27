

# MSCS-532-B01
# Assisgnment 1 
# By Shreyas More 


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr
    

data = [5, 2, 90, 1, 500, -6]
print("Original array:", data)
result = insertionSort(data)
print("Sorted in descending order:", result)