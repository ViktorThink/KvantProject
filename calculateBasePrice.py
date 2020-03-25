import openpyxl
import traceback
#workbook = openpyxl.load_workbook(filename=r"C:\Users\Vikto\OneDrive\Dokument\Excel dokument\Stålaffären sheet 1.xlsx")

sheets = workbook.sheetnames
sheet = workbook.active
sheet2=workbook[sheets[1]]

def calculateBaseMarigin(indexes=range(4,218888)):
    numerDict={}
    for row in range(4,39256):
        numerDict[str(sheet2["B"+str(row)].value)] = sheet2["C"+str(row)].value
    
    money=0
    for j in indexes:#(4,218888):
        basePrice= float(sheet["X"+str(j)].value)
        weight=sheet["AE"+str(j)].value*1000 #float
        productNumber=s=str(sheet["Q"+str(j)].value)
        kurs=sheet["AC"+str(j)].value/sheet["AD"+str(j)].value
    
        try:
            #print("Base price: "+str(basePrice*weight*kurs*0.001))
            #print("Cost: "+str(int(numerDict[productNumber])*weight))
            moneyAdd=float(basePrice*kurs*weight*0.001)-float(numerDict[productNumber])*weight
            #print(moneyAdd)
            money=money+moneyAdd
        except Exception as e:
            print(e)
            traceback.print_exc()
            print(j)
            
    print(money)

calculateBaseMarigin()