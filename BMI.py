import cmath
import time
import os
from fileinput import close
def clear():
    os.system("cls")

def measurements():
    global measurementW
    global measurementH
    measurementW = input("what weight measurement would you like to use? \nkilograms  \nnewtons \ngrams \npounds \nstone \n\n")
    measurementW = measurementW.lower()
    measurementH = input("What height measurement would you like to use? \nmeters \ncentimeters \nfeet \ninches \n\n")
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

def bmicalc():
    global selector
    global bmi
    selector = 0
    bmi = weight/height**2
    print("your bmi is", bmi)
    f = open("BMI.txt", "w")
    f.write("your bmi is " + str(bmi))
    f.close()
    if bmi > 30:
        print("you are clinically obese!")
        selector = "1"
    if bmi < 18.5:
        print("you are one skinny thing, try to gain a bit of weight pls even though you probably wont")
        selector = "2"
    if bmi > 18.5 and bmi < 25:
        print("you are just right! GOOD JOB GOLDILOCKS!")
        selector = "3"
    if bmi > 25 and bmi < 30:
        print("you are a little chubby, maybe lay off the pringles once in a while!")
        selector = "4"

    save = input("would you like to save the results to file? (Y/N)\n")
    if save == "N":
        os.remove("BMI.txt")
        print("files have not been saved")
    if save == "Y":
        print("File Saved!")
    info()
    close()

def info():
    info = input("would you like any further information? (Y/N)\n") #yes I will actually write something normal for these but quite frankly I am lazy. Yes this is the most logical solution I dont care it was the one that came to my mind numbers are useful
    info = info.upper()
    if info == "Y":
        if selector == "1":
            print("okay! Fat")
        if selector == "2":
            print("skinny booger")
        if selector == "3":
            print("perfecto!")
        if selector == "4":
            print("lay off the pringelesl")
    if info == "N":
        pass

def close():
    close = input("would you like to close the program? \n(Y/N) \n")
    close = close.upper()
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