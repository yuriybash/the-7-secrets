def isASubsetOf(list1, list2):
    for elem in list1:
        if (not elem in list2):
            return False
    return True
    

testList1 = ['commit','haaa']
testList2 = ['commit','rebase','push','blame']
print(isASubsetOf(testList1, testList2))
