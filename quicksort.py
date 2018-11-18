#Program by Edgar Daniel Rojas Vazquez
def sortFunc(lista):
    newList = []; # Create Empty List to store sorted list
    if len(lista) <= 1: # If length is 1 or less, return the element or empty list
        return lista
    else: # Else, do the quicksort algorithm, setting a pivot and sorting numbers less than
        # less than the pivot to the left and more to the right
        # all of this is done with a comprehension list for each case.
        newList.extend(sortFunc([s for s in lista[1:] if s<lista[0]]))
        newList.append(lista[0])
        newList.extend(sortFunc([s for s in lista[1:] if s>=lista[0]]))
    return newList # Return the new list

listToSort = [5,4,3,2,1,'c',1,2,3,4,5] # Get our list values
listToSort = [int(s) if str(s).isdigit() else 0 for s in listToSort] # Remove any symbols using a comprehension list
listToSort = sortFunc(listToSort) # Call the function
print(listToSort); # Print results

# The easy way to do it
def sortFuncNormalPerson(lista):
    lista.sort();
    return lista
