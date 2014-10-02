# -*- coding: cp1252 -*-
num1 = int(input("Lägg till första siffran: "))
num2 = int(input("Lägg till andra siffran: "))

def plus(x, y):
    return x + y
print "Plus"
print(num1 + num2)


def minus(x, y):
    return x - y
print "Minus"
print (num1 - num2)


def division(x,y):
    return x / y
print "Dividerat"
print (num1 / num2)


def multiplikation(x,y):
    return x * y
print "Multiplicerat"
print (num1 * num2)
