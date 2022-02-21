
# function to verify if the sortedList is correct
def verify(unsortedarr, sortedList):

    unsortedarr.sort()  # using in-built sorting to sort the list

    # for each item in the two lists verify that the numbers are same
    for i in range(len(sortedList)):
        if sortedList[i] != unsortedarr[i]: 
            return False    # Failed, the sorted list is not correct
    return True # Success, sorted list is correct!
