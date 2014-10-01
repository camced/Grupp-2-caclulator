# -*- coding: cp1252 -*-

#Calculator
#plus
def plus(x, y):

   return x + y

#minus
def minus(x, y):

   return x - y

#multiplikation
def multiplikation(x, y):

   return x * y

#division
def division(x, y):

  return x / y

#medeltal
def medeltal(x, y, z):

  return x + y / z

#median
#def median:

# return 

#summa
#def summa:

#  return

#upphöjt
#def upphöjt:

#  return


print("Välj räknesätt.")
print("1.Plus")
print("2.Minus")
print("3.Mutiplikation")
print("4.Division")
print("5.Medeltal")
print("6.Median")
print("7.Summa flera tal")
print("8.Upphöjt till")
choice = input("Välj(1/2/3/4/5/6/7/8):")

num1 = int(input("Skriv första siffran: "))
num2 = int(input("Skriv andra siffran: "))

if choice == '1':
   print(num1,"+",num2,"=", plus(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", minus(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiplikation(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", division(num1,num2))
   
elif choice == '5':
   print(num1,"/",num2,"=", medeltal(num1,num2))

elif choice == '6':
   print(num1,"/",num2,"=", median(num1,num2))

elif choice == '7':
   print(num1,"/",num2,"=", summa(num1,num2))

elif choice == '8':
   print(num1,"/",num2,"=", upphojt(num1,num2))

else:
   print("Invalid input")
