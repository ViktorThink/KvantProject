from calculateBaseMarigin import calculateBaseMarigin
from getRowOfCustomers import getRowOfCustomers
from listCustomersWithSales import listCustomersWithSales
from topCompanies import topCompanies
from ordersPerProduct import ordersPerProduct
import openpyxl
#workbook = openpyxl.load_workbook(filename=r"C:\Users\Vikto\OneDrive\Dokument\Excel dokument\Stålaffären sheet 1.xlsx")


sheet = workbook.active
sheet2=workbook.worksheets[1]
sheet3=workbook.worksheets[2]




ordersPerProductDict = ordersPerProduct(sheet,sheet2)

#customersWithSalesDict=listCustomersWithSales(sheet,sheet2) 
#top5CustomerDictWithSales=topCompanies(customersWithSalesDict) #second argument decides number of top companies, eg top 5
#rows=getRowOfCustomers(sheet,sheet2) #Can add customer name

#baseMarigin = calculateBaseMarigin(sheet,sheet2)
#print(baseMarigin)