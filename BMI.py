import cmath
import time
import os
from fileinput import close
import sys
def clear():
    os.system("cls")

def type():
    global string
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

def measurements():
    global string
    global measurementW
    global measurementH
    measurementW = input("what weight measurement would you like to use? \nkilograms  \nnewtons \ngrams \npounds \nstone \n\n")
    measurementW = measurementW.lower()
    measurementH = input("What height measurement would you like to use? \nmeters \ncentimeters \nfeet \ninches \nsmoots \nlight years \n\n")
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
    if measurementW == "grams":
        weight = float(input("Please enter your weight: "))
        weight = weight/1000
    if measurementW == "pounds":
        weight = float(input("Please enter your weight: "))
        weight = weight/2.205
    if measurementW == "stone":
        weight = float(input("Please enter your weight: "))
        weight = weight*6.35
    if measurementH == "meters":
        height = float(input("Please enter your height: "))
    if measurementH == "centimeters":
        height = float(input("Please enter your height: "))
        height = height/100
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
    if measurementH == "smoots":
        height = float(input("Please enter your height: "))
        height = height*1.702
    if measurementH == "light years":
        height = float(input("Please enter the base number: "))
        height = height**-16
        height = height*9460730472580044 #this currently doesnt function well on account of me being slightly special and unable to input calculations, maybe unsupported, maybe needs a module WHO KNOWS
    bmicalc()

def bmicalc():
    global selector
    global bmi
    global string
    selector = 0
    bmi = weight/height**2
    print("your bmi is", bmi)
    f = open("BMI.txt", "w")
    f.write("your bmi is " + str(bmi))
    f.close()
    if bmi > 30:
        string="you are clinically obese!"
        type()
        selector = "1"
    if bmi < 18.5:
        string="you are one skinny thing, try to gain a bit of weight pls even though you probably wont"
        type()
        selector = "2"
    if bmi > 18.5 and bmi < 25:
        string="you are just right! GOOD JOB GOLDILOCKS!"
        type()
        selector = "3"
    if bmi > 25 and bmi < 30:
        string="you are a little chubby, maybe lay off the pringles once in a while!"
        type()
        selector = "4"
    string ="\nwould you like to save the results to file? (Y/N)\n"
    type()
    save = input()
    if save == "N":
        os.remove("BMI.txt")
        print("files have not been saved")
    if save == "Y":
        print("File Saved!")
    info()
    close()

def info():
    global string
    string="would you like any further information? (Y/N)\n"
    type()
    info = input()
    info = info.upper()
    if info == "Y":
        if selector == "1":
            string= "Alright so, you are a literal chonker, I would recommend not being fat because well there are a multitude of reasons really!\nWell first of all, lets be honest it looks damned ugly if I am perfectly honest just like dont\nMOREOVER YOU MIGHT GET HEART DISEASES AND DIABETES AND ALL THAT JAZZ SO MAYBE AVOID THAT BUT FRANKLY NOT AS IMPORTANT AS NOT ACHIEVING THE ULTIMATE DRIP IF I AM PERFECLY HONEST."
            type()
        if selector == "2":
           string="skinny booger\n"
           type()
        if selector == "3":
            string="perfecto!"
            type()
        if selector == "4":
            string="lay off the pringeles!"
            type()
    if info == "N":
        pass

def close():
    global string
    string="would you like to close the program? \n(Y/N) \n"
    type()
    close = input()
    close = close.upper()
    if close == "Y":
        string="closing program"
        type()
        time.sleep(1)
        clear()
        exit()
    if close == "N":
        string="looping program"
        type()
        time.sleep(1)
        clear()
        measurements()

clear()
measurements()