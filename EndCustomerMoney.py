import openpyxl
#workbook = openpyxl.load_workbook(filename=r"C:\Users\Vikto\OneDrive\Dokument\Excel dokument\Stålaffären sheet 1.xlsx")

sheet = workbook.active
a={}
for j in range(4,218888):
    i= sheet["K"+str(j)].value
    try:
        money=int(sheet["AC"+str(j)].value)
    except:
        print(j)
        
    if i in a:
        a[i]=a[i]+money
    else:
        a[i]=money
        
for i in a.keys():
    print(str(i)+" "+str(a[i]))