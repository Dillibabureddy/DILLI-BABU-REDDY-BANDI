print("HELLO! WELCOME TO OUR CURRENCY CONVERTOR")
print("Select one from below")
print("Enter 1 : Rupee")
#if 1 is entered you are opting to convert Rupee currency to Dollar,Pound and Euro
print("Enter 2 : Dollar")
#if 2 is entered you are opting to convert Dollar currency to Rupee,Pound and Euro
print("Enter 3 : Pound")
#if 3 is entered you are opting to convert Pound currency to Rupee,Pound and Euro
print("Enter 4 : Euro")
#if 4 is entered you are opting to convert Euro currency to Rupee,Dollar and Pound
a = int(input("Enter your choice : "))
amount = int(input("Enter the amount to be converted : "))
print("The amount to be converted is", amount)

if (a == 1): 
    dollar = amount / 82.31
    print(amount,"Rupee ===> {:.2f} Dollar".format(dollar))
    pound = amount / 101.03
    print(amount,"Rupee ===> {:.2f} Pound".format(pound))
    euro = amount / 86.95
    print(amount,"Rupee ===> {:.2f} Euro".format(euro))
    
elif (a == 2):
    rupee = amount * 82.31
    print(amount,"Dollar ===> {:.2f} Rupee".format(rupee))
    pound = amount *  0.82
    print(amount,"Dollar ===> {:.2f} Pound".format(pound))
    euro = amount * 0.95
    print(amount,"Dollar ===> {:.2f} Euro".format(euro))

elif (a == 3):
    rupee = amount * 101
    print(amount,"Pound ===> {:.2f} Rupee".format(rupee))
    dollar = amount * 1.23
    print(amount,"Pound ===> {:.2f} Dollar".format(dollar))
    euro = amount * 1.16
    print(amount,"Pound ===> {:.2f}  Euro".format(euro))

elif (a == 4):
    rupee = amount * 86.90
    print(amount,"Euro ===> {:.2f} Rupee".format(rupee))
    dollar = amount * 1.06
    print(amount,"Euro ===> {:.2f} Dollar".format(dollar))
    pound = amount * 0.86
    print(amount,"Euro ===> {:.2f} Pound".format(pound))
    
else:
    print("_InvalidInput_TRY AGAIN ")
    
print("              ***** THANK YOU *****               ")
