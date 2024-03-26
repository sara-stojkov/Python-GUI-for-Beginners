# This is going to be a simple GUI weight converter app
import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


def conversion_from_kg(entry_value):
    kgs = float(entry_value.get())
    gram = kgs * 1000
    pounds = kgs * 2.20462
    ounces = kgs * 35.274
    text1.delete("1.0", END)
    text1.insert(END, gram)
    text2.delete("1.0", END)
    text2.insert(END, pounds)
    text3.delete("1.0", END)
    text3.insert(END, ounces)


root = customtkinter.CTk()
root.geometry("600*400")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=10, pady=10)
frame.configure(width=600)

label1 = customtkinter.CTkLabel(master=frame, text="Input the weight in kilograms KG", font=("Arial", 18))
# label1.pack(padx=10, pady=10)

entry_value = StringVar()
entry = customtkinter.CTkEntry(master=frame, placeholder_text="Enter the value", textvariable=entry_value, width=150)
# entry.pack()

label2 = customtkinter.CTkLabel(master=frame, text="Gram")
# label2.pack()

label3 = customtkinter.CTkLabel(master=frame, text="Pound")
# label3.pack()

label4 = customtkinter.CTkLabel(master=frame, text="Ounce")
# label4.pack()

text1 = customtkinter.CTkTextbox(master=frame, height=5, width=100)
text2 = customtkinter.CTkTextbox(master=frame, height=5, width=100)
text3 = customtkinter.CTkTextbox(master=frame, height=5, width=100)

button = customtkinter.CTkButton(master=frame, text="Convert", command=lambda:conversion_from_kg(entry_value))

label1.grid(row=0, column=0)
entry.grid(row=0, column=1)
label2.grid(row=1, column=0)
label3.grid(row=1, column=1)
label4.grid(row=1, column=2)
text1.grid(row=2, column=0)
text2.grid(row=2, column=1)
text3.grid(row=2, column=2)
button.grid(row=0, column=2)

root.mainloop()

