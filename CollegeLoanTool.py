#Jonathan Wray
#College Loan Tool
#Takes In Pay, Hours, Spending, Loan Amount, Years, and APR, and Determines If You Can Affors the Loan

#Imports the Basics For the GUI and OS Checks
import os
import platform
import tkinter

#Imports An Improved tkinter Feature Set, and Confirms All Requirements Are Met By OS
try:
    import customtkinter as gui
except  ImportError as install:
    if platform.system() == "Windows":
        os.system("pip install customtkinter")
        os.system("CollegeLoanTool.py")
        exit()
    else:
        os.system("pip install customtkinter --break-system-packages")
        os.system("python3 CollegeLoanTool.py")
        exit()

#Configures the Window Resolution, Dark Theme, and Title
window = gui.CTk()
window.geometry("1100x500")
window.resizable(width=False, height=False)
window.title("College Loan Tool")
gui.set_appearance_mode("dark")
gui.set_default_color_theme("blue")

#Configures the Grid System Used To Manipulate Widget Locations
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure((2,3), weight=0)
window.grid_rowconfigure((0,1,2), weight=1)

#GUI For the Side View Frame
window.sidebar_frame = gui.CTkFrame(window, width=300, corner_radius=20)
window.sidebar_frame.grid(row=0, column=0, rowspan=4, stick="nsew")

#Default Variable Definition For the Display
Pay = 0
Hours = 0
Spending = 0
Loan = 75000
APR = 10
Years = 25
Loan_Final = 0
Bank_Final = 0
Can_Afford = "Invalid Values"

#Begin List Of Display Elements For Left View
window.tool_label = gui.CTkLabel(window.sidebar_frame, text="College Loan Calculator", font=gui.CTkFont(size=20, weight="bold"))
window.tool_label.grid(row=0, column=0, padx=20, pady=(20,10))

window.pay_label = gui.CTkLabel(window.sidebar_frame, text=Pay, font=gui.CTkFont(size=20, weight="bold"))
window.pay_label.grid(row=1, column=0, padx=20, pady=20)

window.hours_label = gui.CTkLabel(window.sidebar_frame, text=Hours, font=gui.CTkFont(size=20, weight="bold"))
window.hours_label.grid(row=2, column=0, padx=20, pady=20)

window.spending_label = gui.CTkLabel(window.sidebar_frame, text=Spending, font=gui.CTkFont(size=20, weight="bold"))
window.spending_label.grid(row=3, column=0, padx=20, pady=(20,20))

window.loan_label = gui.CTkLabel(window.sidebar_frame, text=Loan, font=gui.CTkFont(size=20, weight="bold"))
window.loan_label.grid(row=4, column=0, padx=20, pady=(0,20))

window.apr_label = gui.CTkLabel(window.sidebar_frame, text=APR, font=gui.CTkFont(size=20, weight="bold"))
window.apr_label.grid(row=5, column=0, padx=20, pady=(40,20))

window.year_label = gui.CTkLabel(window.sidebar_frame, text=Years, font=gui.CTkFont(size=20, weight="bold"))
window.year_label.grid(row=6, column=0, padx=20, pady=(40,20))

#Create a Frame For the Job Portion of Data Entry
window.job_frame = gui.CTkFrame(window, width=300, corner_radius=20)
window.job_frame.grid(row=0, column=1, padx=10, pady=10, stick="new")

#Creates Input Widgets For Pay, Hours, and Spending
window.pay_entry_label = gui.CTkLabel(window.job_frame, text="Hourly Pay", font=gui.CTkFont(size=20, weight="bold"))
window.pay_entry_label.grid(row=0, column=0, padx=10, pady=20)

window.hours_entry_label = gui.CTkLabel(window.job_frame, text="Hours Per Week", font=gui.CTkFont(size=20, weight="bold"))
window.hours_entry_label.grid(row=1, column=0, padx=10, pady=20)

window.spending_entry_label = gui.CTkLabel(window.job_frame, text="Monthly Spending", font=gui.CTkFont(size=20, weight="bold"))
window.spending_entry_label.grid(row=2, column=0, padx=10, pady=20)

window.pay_entry = gui.CTkEntry(window.job_frame, placeholder_text="Placeholder")
window.pay_entry.grid(row=0, column=1, pady=20)

window.hours_entry = gui.CTkEntry(window.job_frame, placeholder_text="Placeholder")
window.hours_entry.grid(row=1, column=1, pady=20)

window.spending_entry = gui.CTkEntry(window.job_frame, placeholder_text="Placeholder")
window.spending_entry.grid(row=2, column=1, pady=20)

#Create Widgets Within the Same Frame to Dislpay Final Calculations
window.loan_final_label = gui.CTkLabel(window.job_frame, text=("Total Value: ", Loan_Final), font=gui.CTkFont(size=20, weight="bold"))
window.loan_final_label.grid(row=0, column=2, padx=20, stick="w")

window.bank_final_label = gui.CTkLabel(window.job_frame, text=("Money After Payments: ", Bank_Final), font=gui.CTkFont(size=20, weight="bold"))
window.bank_final_label.grid(row=1, column=2, padx=20, stick="w")

window.can_afford_label = gui.CTkLabel(window.job_frame, text=Can_Afford, font = gui.CTkFont(size=20, weight="bold"))
window.can_afford_label.grid(row=2, column=2, padx=20, stick="w")

#Creates A Frame For the Loan Portion of Data Entry
window.loan_frame = gui.CTkFrame(window, width=300, height=260, corner_radius=20)
window.loan_frame.grid(row=1, column=1, padx=10, stick="nsew")

#Creates Input Widgets For Loan Amount, Loan APR, and Loan Years
window.slider_loan = gui.CTkSlider(window.loan_frame, from_=0, to=150000, number_of_steps=150, width=780)
window.slider_loan.grid(row=0, column=0, padx=10, pady=(30,55), stick="w")

window.slider_apr = gui.CTkSlider(window.loan_frame, from_=0, to=20, number_of_steps=40, width=780)
window.slider_apr.grid(row=1, column=0, padx=10, pady=(20,55), stick="w")

window.slider_years = gui.CTkSlider(window.loan_frame, from_=1, to=50, number_of_steps=49, width=780)
window.slider_years.grid(row=2, column=0, padx=10, pady=(20,20), stick="w")

#Defines Functions Related To Each Value Input, and Update the Left View Stats
def update_pay():
    Pay = window.pay_entry.get()
    
    if len(Pay) > 0 and len(Pay) < 10 and float(Pay) >= 0 and Pay.isalpha() == False:
        window.pay_label.configure(text=Pay)
        window.pay_label.after(25, update_pay)
    else:
        window.pay_label.configure(text="Invalid")
        window.pay_label.after(25, update_pay)
    
def update_hours():
    Hours = window.hours_entry.get()
    
    if len(Hours) > 0 and len(Hours) < 10 and float(Hours) <= 168 and float(Hours) >= 0 and Hours.isalpha() == False:
        window.hours_label.configure(text=Hours)
        window.hours_label.after(25, update_hours)
    else:
        window.hours_label.configure(text="Invalid")
        window.hours_label.after(25, update_hours)

def update_spending():
    Spending = window.spending_entry.get()

    if len(Spending) > 0 and len(Spending) < 10 and float(Spending) >= 0 and Spending.isalpha() == False:
        window.spending_label.configure(text=Spending)
        window.spending_label.after(25, update_spending)
    else:
        window.spending_label.configure(text="Invalid")
        window.spending_label.after(25, update_spending)

def update_loan():
    Loan = window.slider_loan.get()
    window.loan_label.configure(text=("$", Loan))
    window.loan_label.after(25, update_loan)

def update_apr():
    APR = window.slider_apr.get()
    window.apr_label.configure(text=(APR, "% APR"))
    window.apr_label.after(25, update_apr)

def update_years():
    Years = window.slider_years.get()
    window.year_label.configure(text=(Years, "Years"))
    window.year_label.after(25, update_years)

def update_loan_final():
    global Loan_Final
    Loan_Final = window.slider_loan.get() * (1 + (window.slider_apr.get() / 100)) ** window.slider_years.get()
    window.loan_final_label.configure(text=("Value: $", round(Loan_Final, 2)))
    window.loan_final_label.after(25, update_loan_final)
    
def update_bank_final():
    try:
        global Bank_Final
        Bank_Final = ((float(window.pay_entry.get()) * float(window.hours_entry.get())) * 4) - (Loan_Final / (12 * window.slider_years.get())) - float(window.spending_entry.get())
        window.bank_final_label.configure(text=("Money After Payments: $", round(Bank_Final, 2)))
        window.bank_final_label.after(25, update_bank_final)
    except ValueError:
        window.bank_final_label.configure(text="Invalid Values")
        window.bank_final_label.after(25, update_bank_final)

def update_can_afford():
    try:
        if Bank_Final >= 0:
            window.can_afford_label.configure(text="You Can Afford the Loan")
        elif Bank_Final < 0:
            window.can_afford_label.configure(text="You Cannot Afford the Loan")
        window.can_afford_label.after(25, update_can_afford)
    except:
        window.can_afford_label.configure(text="Invalid Values")
        window.can_afford_label.after(25, update_can_afford)

#Call Functions To Update the Values Displayed In the Left View
update_pay()
update_hours()
update_spending()
update_loan()
update_apr()
update_years()

update_loan_final()
update_bank_final()
update_can_afford()

window.mainloop()
