#python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(mylist):

    # Traverse through 1 to len(arr)
    for i in range(1, len(mylist)):

        key = myList[i]

        # Move elements of arr [0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < mylist[j] :
            myList[j+1] = myList[j]
            j -= 1
        myList[j+1] = key

# Driver code to test above
myList = [12, 11, 13, 5, 6, 7, 1]
insertionSort(myList)
print(" sorted array is: ")
for i in range(len(myList)):
    print(myList[i])