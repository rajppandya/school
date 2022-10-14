"""Defines product inventory inputed by user"""

import random

#in the following we will define the attributes 
class Product():
    def __init__(self, name, codes, price, cost, stock, units):
        self.name = name
        self.codes = codes
        self.price = price
        self.cost = cost
        self.stock = stock
        self.units= units
    def showProducts(self):
        print("Name == :",self.name, "\nCodes == :",self.codes, "\nPrice == :",self.price,
        "\nCost == :",self.cost, "\nStock == :",self.stock, "\nUnits == :", self.units)
    
#having a display intro for looks.
def displayintro():
    print("-------------------------------------")
    print("--                                 --")
    print("--                                 --")
    print("--           Veiw Product          --")
    print("--            Inventory            --")
    print("--                                 --")
    print("--                                 --")
    print("-------------------------------------")
displayintro()

#Now we will be executing while loops to allow the following code to be repeated
#We will also be adding if statements to make sure we only get the desired input
def getInput():
    validName, validCode, validPrice, validCost, validStock, validUnits = False, False, False, False, False,False
    listReturn = []

    while validName == False:
        name = input("Enter Product Name:")
        listReturn.append(name)
        validName = True

    while validCode == False:
        codes = int(input("Enter Product Code:"))
        if codes >= 100 and codes <= 1000:
            listReturn.append(codes)
            validCode = True
        else:
            print("Inccorect Code,Enter Valid Code between 100 and 1000")
            validCode = False
    
    while validPrice == False:
        price = float(input("Enter Product Price:"))
        if price > 1:
            listReturn.append(price)
            validPrice = True
        else:
            print("Enter Correct Price:")
            validPrice = False
    
    while validCost == False:
        cost = float(input("Enter Manufacturing Cost:"))
        if cost > 1:
            listReturn.append(cost)
            validCost = True
        else:
            print("Enter Correct Manufacturing Cost:")
            validCost = False

    while validStock == False:
        stock = int(input("Enter Valid Stock Level:"))
        if stock > 0: 
            listReturn.append(stock)
            validStock = True
        else:
            print("Enter Valid Stock Level:")
            validStock = False

    while validUnits == False:
        units = int(input("Enter Product Units:"))
        if units >= 0:
            listReturn.append(units)
            validUnits = True
        else:
            print("Enter Valid Monthly Units Manufactored:")
            validUnits = False

    return listReturn

productInfo = getInput()
item = Product(productInfo[0],productInfo[1],productInfo[2],productInfo[3],productInfo[4],productInfo[5])

totalSales = 0
for i in range(1,13):
    print("----------------------------------------")
    print("Month:", i)
    print("Units Manufactured: ",item.units, "units")
    item.stock = item.stock + item.units
    monthSales = random.randint((item.units - 10),(item.units +10))
    totalSales += monthSales
    print("Old Stock:", item.stock, "\nSales:",monthSales)
    item.stock = item.stock - monthSales
    print("New Stock: ", item.stock)
    print("----------------------------------------")
print("TOTAL PROFIT == $",((totalSales * item.price)-((item.units * 12)* item.cost)))


