#Jonathan Wray
#College Loan Budgeting Tool
#Calculates Loan Interest and Takes Current Pay to Determine if You Can Afford a Loan

import os
import tkinter

OS = str(input("Do you use Windows or Linux?"))

if OS == "Windows":
    os.system("WindowsSetup.bat")

if OS == "Linux":
    os.system("./LinuxSetup.sh")
