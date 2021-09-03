#!/usr/bin/env python3

#Handle exeptions

while True:
    try:
        x = int(input("Please enter a number:\n"))
        print("The number entered is: ", x)
        break
    except ValueError:
        print ("Oops!  this is not valid. Try again...")
