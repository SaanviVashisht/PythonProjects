def getGreatestNumber(numbersList):
    biggest = numbersList[0][0]
    for x in numbersList[0]:
        if(x>=biggest):
            biggest=x
    return biggest

def getProduct(numbersList):
    product=1
    for x in numbersList[1]:
        product=product*x
    return product
    
favNum=int(input('Please enter a number: '))
numbersList=[[1,3,2],[2,6,4],12]
maxNum=getGreatestNumber(numbersList)
print(maxNum)
prodNum=getProduct(numbersList)
print(prodNum)

if numbersList[2]%2==0:
    print(maxNum%favNum,prodNum%favNum)
else:
    print('Have a good day!')



   