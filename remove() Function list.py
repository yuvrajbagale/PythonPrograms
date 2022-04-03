#remove() Function:- we can use remove() function remove specified items from the list. if the item present multiple times then only first occurrence will be removed.
n=[10,20,30,10]
n.remove(10)
#n.remove(40) >> ValueError: list.remove(x): x not in list
print(n)

# Note - before useing remove function fist we have to check specified element present in the list or not by using in opreter. 