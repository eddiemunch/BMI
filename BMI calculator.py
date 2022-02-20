import cmath
import time
import os
from fileinput import close
def clear():
    os.system("cls")

def bmicalc():
    bmi = weight/height**2
    print("your bmi is", bmi)
    if bmi > 30:
        print("you are clinically obese!")
    if bmi < 18.5:
        print("you are one skinny thing, try to gain a bit of weight pls even though you probably wont")
    if bmi > 18.5 and bmi < 25:
        print("you are just right! GOOD JOB GOLDILOCKS!")
    if bmi > 25 and bmi < 30: print("you are a little chubby, maybe lay off the pringles once in a while!")
def measurements():
    global measurementW
    global measurementH
    measurementW = input("what weight measurement would you like to use? \nkilograms  \nnewtons \ngrams \n")
    measurementW = measurementW.lower()
    measurementH = input("What height measurement would you like to use? \nmeters \ncentimeters \n")
    measurementH = measurementH.lower()
    inputs()

def inputs():
    global weight
    global height
    if measurementW == "kilograms":
        weight = float(input("Please Input your weight: "))
    if measurementW == "newtons":
        weight = float(input("Please Input your weight: "))
        weight = weight/9.81
    if measurementH == "meters":
        height = float(input("Please enter your height: "))
    if measurementH == "centimeters":
        height = float(input("Please enter your height: "))
        height = height/100
    if measurementW == "grams":
        weight = float(input("Please enter your weight: "))
        weight = weight/1000
    bmicalc()
    choice()

def choice():
    global close
    close = input("would you like to close the program? \n(Y/N) ")
    if close == "Y":
        print("closing program")
        time.sleep(1)
        clear()
        exit()
    if close == "N":
        print("looping program")
        time.sleep(1)
        clear()
        measurements()
clear()
measurements()