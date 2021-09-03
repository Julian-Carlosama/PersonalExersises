#!/usr/bin/python3

#Funtion that allow multiple two numbers

def multiplic(a, b):
    numbers = a * b
    print("The result between this numbers is: ",numbers)


#Get two numbers to process
num1 = int(input("Ingrese el primer numero a multiplcar. \n"))
num2 = int(input("Ingrese el segundo numero a multiplcar. \n"))

multiplic(num1,num2) #Call the function and pased two numbers


#Functions that get a number, print a multiplication table
def multTable(y):

    for n in range(1,11):
        print(y,  "*", n, "=", n*y)


#Get a number to show multiplication table
number = int(input("Ingrese un número a multiplcar. \n"))

multTable(number) #Call the function and add a argument to process
