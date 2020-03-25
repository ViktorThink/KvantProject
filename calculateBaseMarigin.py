def calculateBaseMarigin(sheet, sheet2, indexes=range(4,218888)):
    numerDict={}
    for row in range(4,39256):
        cost=sheet2["C"+str(row)].value
        number=str(sheet2["B"+str(row)].value)
        numerDict[number] = cost
    
    money=0
    for j in indexes:#(4,218888):
        basePrice= float(sheet["X"+str(j)].value)
        weight=sheet["AE"+str(j)].value*1000 #float
        productNumber=str(sheet["Q"+str(j)].value)
        kurs=sheet["AC"+str(j)].value/sheet["AD"+str(j)].value
    
        try:
            #print("Base price: "+str(basePrice*weight*kurs*0.001))
            #print("Cost: "+str(int(numerDict[productNumber])*weight))
            moneyAdd=float(basePrice*kurs*weight*0.001)-float(numerDict[productNumber])*weight
            #print(moneyAdd)
            money=money+moneyAdd
        except Exception as e:
            print("An error occured: "+str(e))

            
    return money


