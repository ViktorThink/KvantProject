import openpyxl
#workbook = openpyxl.load_workbook(filename=r"C:\Users\Vikto\OneDrive\Dokument\Excel dokument\Stålaffären sheet 1.xlsx")

sheets = workbook.sheetnames
sheet = workbook.active
sheet2=sheets[1]
a={}
for j in range(4,218888):
    if sheet["K"+str(j)].value == customerName:
        i= sheet["X"+str(j)].value
        s=sheet["AE"+str(j)].value*1000*sheet2["AE"+str(j)]
        try:
            money=int(i)-int(s)
        except:
            print(j)
        
print(money)