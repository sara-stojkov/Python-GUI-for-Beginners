import customtkinter

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")


def addition():
    num1 = entry1.get()
    num2 = entry2.get()
    if num1 and num2:
        sum = int(num1) + int(num2)
        sum_label = customtkinter.CTkLabel(master=frame, text="Rezultat je " + str(sum))
        sum_label.pack(padx=12, pady=10)


def subtraction():
    num1 = entry1.get()
    num2 = entry2.get()
    if num1 and num2:
        sum = int(num1) - int(num2)
        sum_label = customtkinter.CTkLabel(master=frame, text="Rezultat je " + str(sum))
        sum_label.pack(padx=12, pady=10)

root = customtkinter.CTk()  # kreiramo objekat
root.geometry("800x600")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=12, pady=10)
frame.configure(width=500)

label = customtkinter.CTkLabel(master=frame, text="Calculator", font=("Arial", 20))
label.pack(padx=12, pady=10)
label.configure(width=400)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="First Number", font=("Arial", 20))
entry1.pack(padx=12, pady=10)
entry1.configure(width=300)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Second Number", font=("Arial", 20))
entry2.pack(padx=12, pady=10)
entry2.configure(width=400)

button_plus = customtkinter.CTkButton(master=frame, text="+", command=addition, font=("Arial", 20))
button_plus.pack(padx=12, pady=10)

button_minus = customtkinter.CTkButton(master=frame, text="-", command=subtraction, font=("Arial", 20))
button_minus.pack(padx=12, pady=10)

root.mainloop()

