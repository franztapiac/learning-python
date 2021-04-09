# Lists
# Written by Franz A. Tapia Chaca
# on 14 January 2021

myUniqueList = []
myLeftovers = []

def CollectRejected(addition):
    myLeftovers.append(addition)
    return


def AppendToList(addition):
    if type(addition) == bool:  # if addition is boolean True or False
        if any(x is addition for x in myUniqueList):  # if any element in myUniqueList == boolean addition
            CollectRejected(addition)
            return False
        else:  # if any element in myUniqueList != boolean addition
            myUniqueList.append(addition)
            return True

    else:
        if addition in myUniqueList:
            CollectRejected(addition)
            return False
        else:
            myUniqueList.append(addition)
            return True


# Testing the function
print("test 1: appending integer 1")
print("\tstarting myUniqueList: " + str(myUniqueList))
print("\tstarting myLeftovers: " + str(myLeftovers))
print("\tAppended to myUniqueList? " + str(AppendToList(1)))
print("\tresulting myUniqueList: " + str(myUniqueList))
print("\tresulting myLeftovers: " + str(myLeftovers))

print("\ntest 2: appending integer 1")
print("\tstarting myUniqueList: " + str(myUniqueList))
print("\tstarting myLeftovers: " + str(myLeftovers))
print("\tAppended to myUniqueList? " + str(AppendToList(1)))
print("\tresulting myUniqueList: " + str(myUniqueList))
print("\tresulting myLeftovers: " + str(myLeftovers))

print("\ntest 3: appending float 3.5")
print("\tstarting myUniqueList: " + str(myUniqueList))
print("\tstarting myLeftovers: " + str(myLeftovers))
print("\tAppended to myUniqueList? " + str(AppendToList(3.5)))
print("\tresulting myUniqueList: " + str(myUniqueList))
print("\tresulting myLeftovers: " + str(myLeftovers))

print("\ntest 4: appending string 'Hello'")
print("\tstarting myUniqueList: " + str(myUniqueList))
print("\tstarting myLeftovers: " + str(myLeftovers))
print("\tAppended to myUniqueList? " + str(AppendToList("Hello")))
print("\tresulting myUniqueList: " + str(myUniqueList))
print("\tresulting myLeftovers: " + str(myLeftovers))

print("\ntest 5: appending boolean True")  # doesn't work b/c 1 == True
print("\tstarting myUniqueList: " + str(myUniqueList))
print("\tstarting myLeftovers: " + str(myLeftovers))
print("\tAppended to myUniqueList? " + str(AppendToList(True)))
print("\tresulting myUniqueList: " + str(myUniqueList))
print("\tresulting myLeftovers: " + str(myLeftovers))

print("\ntest 6: appending float 3.5")
print("\tstarting myUniqueList: " + str(myUniqueList))
print("\tstarting myLeftovers: " + str(myLeftovers))
print("\tAppended to myUniqueList? " + str(AppendToList(3.5)))
print("\tresulting myUniqueList: " + str(myUniqueList))
print("\tresulting myLeftovers: " + str(myLeftovers))

print("\ntest 7: appending list [1, 2, 3]")
print("\tstarting myUniqueList: " + str(myUniqueList))
print("\tstarting myLeftovers: " + str(myLeftovers))
print("\tAppended to myUniqueList? " + str(AppendToList([1, 2, 3])))
print("\tresulting myUniqueList: " + str(myUniqueList))
print("\tresulting myLeftovers: " + str(myLeftovers))

print("\ntest 8: appending boolean True")
print("\tstarting myUniqueList: " + str(myUniqueList))
print("\tstarting myLeftovers: " + str(myLeftovers))
print("\tAppended to myUniqueList? " + str(AppendToList(True)))
print("\tresulting myUniqueList: " + str(myUniqueList))
print("\tresulting myLeftovers: " + str(myLeftovers))

print("\ntest 9: appending list [1, 2, 3]")
print("\tstarting myUniqueList: " + str(myUniqueList))
print("\tstarting myLeftovers: " + str(myLeftovers))
print("\tAppended to myUniqueList? " + str(AppendToList([1, 2, 3])))
print("\tresulting myUniqueList: " + str(myUniqueList))
print("\tresulting myLeftovers: " + str(myLeftovers))
