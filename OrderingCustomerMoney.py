
def findBiggest(a):
    biggest=0
    
    for i in a.keys():
        #print(str(i)+" "+str(a[i]))
        if a[i] >biggest:
            biggest=a[i]
            biggestName=i
    return biggestName

def topCompanies(companies,number=5):         
    topCompanies    
    for i in range(number):
        s=findBiggest(companies)
        topCompanies[s]=companies[s]
        print(s+" "+str(companies[s]))
        del companies[s]