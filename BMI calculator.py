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
    measurementW = input("what weight measurement would you like to use? \nkilograms  \nnewtons \ngrams \npounds \nstone \n")
    measurementW = measurementW.lower()
    measurementH = input("What height measurement would you like to use? \nmeters \ncentimeters \nfeet \ninches \n")
    measurementH = measurementH.lower()
    inputs()

def inputs():
    global feet
    global inches
    global kg1
    global kg2
    global weight
    global height
    if measurementW == "kilograms":
        weight = float(input("Please enter your weight: "))
    if measurementW == "newtons":
        weight = float(input("Please enter your weight: "))
        weight = weight/9.81
    if measurementH == "meters":
        height = float(input("Please enter your height: "))
    if measurementH == "centimeters":
        height = float(input("Please enter your height: "))
        height = height/100
    if measurementW == "grams":
        weight = float(input("Please enter your weight: "))
        weight = weight/1000
    if measurementW == "pounds":
        weight = float(input("Please enter your weight: "))
        weight = weight/2.205
    if measurementW == "stone":
        weight = float(input("Please enter your weight: "))
        weight = weight*6.35
    if measurementH == "feet":
        print("for this we will split your height into inches and feet so first: ")
        feet = float(input("Please enter your height (feet excluding inches): "))
        inches = float(input("Please enter your height (the remainder in inches): "))
        kg1 = feet/3.281
        kg2 = inches/39.37
        height = kg1+kg2
    if measurementH == "inches":
        height = float(input("Please enter your height: "))
        height = height/39.37
    bmicalc()
    choice()

def choice():
    global close
    close = input("would you like to close the program? \n(Y/N) \n")
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