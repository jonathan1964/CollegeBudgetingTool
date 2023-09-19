#Jonathan Wray
#College Loan Budgeting Tool
#Calculates Loan Interest and Takes Current Pay to Determine if You Can Afford a Loan

import os
import tkinter
import tkinter.messagebox
import time
import platform
try:
    import customtkinter
except ImportError as install:
    if platform.system() == "Windows":
        os.system("pip install customtkinter")
        os.system("CollegeLoanTool.py")
        exit()
    else
        os.system("pip install customtkinter --break-system-packages")
        os.system("python3 CollegeLoanTool.py")
        exit()

window = customtkinter.CTk()
window.geometry("1100x580")
window.resizable(width=False, height=False)
window.title("College Loan Tool")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure((2,3), weight=0)
window.grid_rowconfigure((0,1,2), weight=1)

window.sidebar_frame = customtkinter.CTkFrame(window, width=140, corner_radius=20)
window.sidebar_frame.grid(row=0, column=0, rowspan=4, stick="nsew")

window.namelabel = customtkinter.CTkLabel(window.sidebar_frame, text="College Loan Calculator", font=customtkinter.CTkFont(size=20, weight="bold"))
window.namelabel.grid(row=0, column=0, padx=20, pady=(20,10))

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

window.pay_label = customtkinter.CTkLabel(window.sidebar_frame, text="pay", font=customtkinter.CTkFont(size=20, weight="bold"))
window.pay_label.grid(row=1, column=0, padx=(20,10), pady=(20,10), stick="s")

window.hours_label = customtkinter.CTkLabel(window.sidebar_frame, text="hours", font=customtkinter.CTkFont(size=20, weight="bold"))
window.hours_label.grid(row=3, column=0, padx=(20,10), pady=(20,10), stick="s")

window.spending_label = customtkinter.CTkLabel(window.sidebar_frame, text="spending", font=customtkinter.CTkFont(size=20, weight="bold"))
window.spending_label.grid(row=5, column=0, padx=(20,10), pady=(20,10), stick="s")

window.spacer_1 = customtkinter.CTkLabel(window.sidebar_frame, text="-", font=customtkinter.CTkFont(size=20, weight="bold"))
window.spacer_1.grid(row=7, column=0, padx=(20,10), pady=(20,10), stick="s")

window.spacer_2 = customtkinter.CTkLabel(window.sidebar_frame, text="-", font=customtkinter.CTkFont(size=20, weight="bold"))
window.spacer_2.grid(row=9, column=0, padx=(20,10), pady=(20,10), stick="s")

Loan = window.slider_loan.get()

window.loan_label = customtkinter.CTkLabel(window.sidebar_frame, text=("$", Loan), font=customtkinter.CTkFont(size=20, weight="bold"))
window.loan_label.grid(row=11, column=0, padx=(20,10), pady=(50,10), sticky="s")

APR = window.slider_apr.get()

window.apr_label = customtkinter.CTkLabel(window.sidebar_frame, text=APR, font=customtkinter.CTkFont(size=20, weight="bold"))
window.apr_label.grid(row=13, column=0, padx=(20,10), pady=(20,10), sticky="s")

Years = window.slider_years.get()

window.year_label = customtkinter.CTkLabel(window.sidebar_frame, text=Years, font=customtkinter.CTkFont(size=20, weight="bold"))
window.year_label.grid(row=15, column=0, padx=(20,10), pady=(20,10), sticky="s")

def update_loan():
    Loan = window.slider_loan.get()
    window.loan_label.configure(text=("$", Loan))
    window.loan_label.after(100, update_loan)

def update_apr():
    APR = window.slider_apr.get()
    window.apr_label.configure(text=APR)
    window.apr_label.after(100, update_apr)

def update_years():
    Years = window.slider_years.get()
    window.year_label.configure(text=Years)
    window.year_label.after(100, update_years)

update_loan()
update_apr()
update_years()

window.mainloop()
