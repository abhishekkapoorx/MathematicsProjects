def bubbleSort(unsortedList: list):
    noOfPasses = len(unsortedList)-1
    sortedList = unsortedList
    for passNo in range(0, noOfPasses):
        # print(f"Pass No.: {passNo}")
        for i in range(len(sortedList)-passNo-1):
            if i!=len(sortedList)-1:
                if sortedList[i]>sortedList[i+1]:
                    gvar = sortedList[i]
                    sortedList[i] = sortedList[i+1]
                    sortedList[i+1] = gvar
                else:
                    continue
            # print(sortedList)
    return sortedList

def LinearSearch(yourList:list, searchNumber:int):
    for index in range(len(yourList)):
        if yourList[index] == searchNumber:
            return [yourList, index]
        else:
            continue
    else:
        return None

def BinarySearch(yourList:list, searchNumber:int):
    sortedList = bubbleSort(yourList)
    start = 0
    end = len(sortedList)-1
    mid = (start + end )//2
    
    while True:
        # print(f"Start: {start} Mid: {mid} End: {end} Search number {searchNumber}")
        if start == end and sortedList[mid]!=searchNumber:
            return None
        elif sortedList[mid]==searchNumber:
            return [yourList, mid]
        elif searchNumber > sortedList[mid]:
            start = mid+1
            mid = (start + end )//2
            continue
        elif searchNumber < sortedList[mid]:
            end = mid-1
            mid = (start + end )//2
            continue
        



if __name__ == "__main__":
    noOfElements = int(input("Enter no of elements you want in your list: "))
    yourList = []
    for ele in range(noOfElements):
        element = int(input(f"Enter Element {ele+1}: "))
        yourList.append(element)
    print(f"Your List: {yourList}")

    searchNumber = int(input("\nEnter number to search: "))
    searchMethod = int(input("\nBy which method you want to search in list?\n\t1. Linear Search\n\t2. Binary Search\n: "))

    # Perform Search using selected methods
    if searchMethod == 1:
        respond = LinearSearch(yourList, searchNumber)

    elif searchMethod == 2:
        respond = BinarySearch(yourList, searchNumber)

    # Print index if found
    if respond is None:
        print(f"Not found {searchNumber} in {yourList}")
    else:
        print(f"Number found at index {respond[1]} in list: {respond[0]}")

