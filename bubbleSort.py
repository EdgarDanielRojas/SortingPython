# Program By Edgar Daniel Rojas Vazquez
def sortFunc(lista):
    newList = []; # Create list where we will store values and a helper list
    temp = [];
    if len(lista) <= 1: # If list is 1 return value or return empty list if empty
        return lista
    else:
        if lista[0]>lista[1]: # If current number is greater than next
            # we append the smaller number first and then we add
            # the next recursive call which will return a bubbled up list
            newList.append(lista[1])
            temp.extend(lista[2:])
            temp.insert(0,lista[0])
            newList.extend(sortFunc(temp))
        else: # If number is less than, we append it first and then 
            # append the next recursive call to the function which
            # will return a bubbled up list
            newList.append(lista[0])
            newList.extend(sortFunc(lista[1:]))
    return newList

listToSort = [5,4,3,2,1,'c',1,2,3,4,5] # Get our list values
listToSort = [int(s) if str(s).isdigit() else 0 for s in listToSort] # Remove any symbols using a comprehension list
for i in range(len(listToSort)): # Iterate the length of the list to ensure
    # all of the elements are sorted
    listToSort = sortFunc(listToSort)
print(listToSort);

# The easy way to do it
def sortFuncNormalPerson(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
