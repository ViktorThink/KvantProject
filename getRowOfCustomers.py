

def getRowOfCustomers(sheet,sheet2,customerName="ROBELTA"):
    customerName="ROBELTA"
    rowsNumbers=[]
    for j in range(4,218888):
        if sheet["K"+str(j)].value == customerName:
            rowsNumbers.append(j)
    return rowsNumbers

