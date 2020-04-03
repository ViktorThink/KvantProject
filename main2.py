from calculateBaseMarigin import calculateBaseMarigin
from getRowOfCustomers import getRowOfCustomers
from listCustomersWithSales import listCustomersWithSales
from topCompanies import topCompanies
import openpyxl
from getAllProducts import getAllProducts

from calculateBaseMarigin import getNumberDict
workbook = openpyxl.load_workbook(filename=r"C:\Users\Vikto\OneDrive\Dokument\Excel dokument\Stålaffären.xlsx")


sheet = workbook.active
sheet2=workbook.worksheets[1]
sheet3=workbook.worksheets[2]





a=getAllProducts(sheet,sheet2)
b={}
for item in a:
    b[item]=0

numberDict=getNumberDict(sheet,sheet2)

customersWithSalesDict=listCustomersWithSales(sheet,sheet2) #in k sek
top5CustomerDictWithSales=topCompanies(customersWithSalesDict) #second argument decides number of top companies, eg top 5

for key in top5CustomerDictWithSales.keys():
    rows=getRowOfCustomers(sheet,sheet2) #Can add customer name
    for row in rows:
        item=sheet["G"+str(row)].value
        b[item]=b[item]+calculateBaseMarigin(sheet,sheet2,range(row,row+1),numberDict)
    print(str(key))
    for key in b:
        print(str(key)+": "+str(b[key]))
        b[key]=0