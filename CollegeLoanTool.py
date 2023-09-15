#Jonathan Wray
#College Loan Budgeting Tool
#Calculates Loan Interest and Takes Current Pay to Determine if You Can Afford a Loan

import os
import tkinter
import tkinter.messagebox

PreReq = 0

while PreReq == 0:

    OS = str(input("Do you use Windows or Linux? "))

    if OS == "Windows":
        os.system("WindowsSetup.bat")
        PreReq = 1
        break;

    if OS == "Linux":
        os.system("./LinuxSetup.sh")
        PreReq = 1
        break;

import customtkinter

window = customtkinter.CTk()
window.geometry("1100x580")
window.resizable(width=False, height=False)
window.title("College Loan Tool")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure((2,3), weight=0)
window.grid_rowconfigure((0,1,2), weight=1)

window.sidebar_frame = customtkinter.CTkFrame(window, width=140, corner_radius=0)
window.sidebar_frame.grid(row=0, column=0, rowspan=4, stick="nsew")

window.namelabel = customtkinter.CTkLabel(window.sidebar_frame, text="College Loan Calculator", font=customtkinter.CTkFont(size=20, weight="bold"))
window.namelabel.grid(row=0, column=0, padx=20, pady=(20,10))

window.loan_label = customtkinter.CTkLabel(window.sidebar_frame, text="Loan", font=customtkinter.CTkFont(size=20, weight="bold"))
window.loan_label.grid(row=3, column=0, padx=20, pady=(20,10), sticky="ew")

window.textframe = customtkinter.CTkFrame(window, width=320)
window.textframe.configure(fg_color="gray8")
window.textframe.grid(row=0, column=1, padx=(20,0), pady=(20,0), sticky="nsw")

window.slider_loan_frame = customtkinter.CTkFrame(window,fg_color="transparent")
window.slider_loan_frame.grid(row=2, column=1, padx=(20,0), pady=(20,0), sticky=("nsew"))
window.slider_loan_frame.grid_columnconfigure(0, weight=1)
window.slider_loan_frame.grid_rowconfigure(4, weight=1)

window.indicator_loan = customtkinter.CTkProgressBar(window.slider_loan_frame)
window.indicator_loan.grid(row=0, column=0, padx=(20,10), pady=(10,10), sticky="ew")
window.slider_loan = customtkinter.CTkSlider(window.slider_loan_frame, from_=0, to=150000, number_of_steps=150)
window.slider_loan.grid(row=0, column=0, padx=(20,10), pady=(10,10), sticky="ew")

window.indicator_apr = customtkinter.CTkProgressBar(window.slider_loan_frame)
window.indicator_apr.grid(row=4, column=0, padx=(20,10), pady=(10,10), sticky="ew")
window.slider_apr = customtkinter.CTkSlider(window.slider_loan_frame, from_=0, to=20, number_of_steps=80)
window.slider_apr.grid(row=4, column=0, padx=(20,10), pady=(10,10), sticky="ew")

window.indicator_years = customtkinter.CTkProgressBar(window.slider_loan_frame)
window.indicator_years.grid(row=8, column=0, padx=(20,10), pady=(10,10), sticky="ew")
window.slider_years = customtkinter.CTkSlider(window.slider_loan_frame, from_=0, to=50, number_of_steps=50)
window.slider_years.grid(row=8, column=0, padx=(20,10), pady=(10,10), sticky="ew")

window.mainloop()

Loan = window.slider_loan.get()
APR = window.slider_apr.get()
Years = window.slider_years.get()
print(Loan)
print(APR)
print(Years)
