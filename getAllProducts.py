def getAllProducts(sheet,sheet2):
    a=[]
    for j in range(4,218888):
        i= sheet["G"+str(j)].value
        if i not in a:
            a.append(i)
    return a