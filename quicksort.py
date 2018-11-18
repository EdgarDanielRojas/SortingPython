def sortFunc(lista):
    newList = [];
    if len(lista) <= 1:
        return lista
    else:
        newList.extend(sortFunc([s for s in lista[1:] if s<lista[0]]))
        newList.append(lista[0])
        newList.extend(sortFunc([s for s in lista[1:] if s>=lista[0]]))
    return newList

listToSort = [5,4,3,2,1,'c',1,2,3,4,5]
listToSort = [int(s) if str(s).isdigit() else 0 for s in listToSort]
listToSort = sortFunc(listToSort)
print(listToSort);

# The easy way to do it
def sortFuncNormalPerson(lista):
    lista.sort();
    return lista
