# Program By Edgar Daniel Rojas Vazquez
def sortFunc(lista):
    newList = [];
    temp = [];
    if len(lista) == 1:
        return lista
    else:
        if lista[0]>lista[1]:
            newList.append(lista[1])
            temp.extend(lista[2:])
            temp.insert(0,lista[0])
            newList.extend(sortFunc(temp))
        else:
            newList.append(lista[0])
            temp.extend(lista[1:])
            newList.extend(sortFunc(temp))
    return newList

listToSort = [5,4,3,2,1,'c']
listToSort = [int(s) if str(s).isdigit() else 0 for s in listToSort]
for i in range(len(listToSort)):
    listToSort = sortFunc(listToSort)
print(listToSort);

# The easy way to do it
def sortFuncNormalPerson(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j]>lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
