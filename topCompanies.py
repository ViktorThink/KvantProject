
def findBiggest(a):
    biggest=0
    
    for i in a.keys():
        #print(str(i)+" "+str(a[i]))
        if a[i] >biggest:
            biggest=a[i]
            biggestName=i
    return biggestName

def topCompanies(companies,number=5):         
    topCompanyDict={}  
    for i in range(number):
        s=findBiggest(companies)
        topCompanyDict[s]=companies[s]
        print(s+" "+str(companies[s]))
        del companies[s]