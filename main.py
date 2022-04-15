from tkinter import *

window = Tk()
window.geometry("400x600")
window.configure(bg="#645853")
listbox = Listbox(window, bg="#645853", font=("Arial", 35,), foreground="white", width=20)
listbox.pack()
listbox.insert(1, "-Pizza $5.00")
listbox.insert(2, "-Hamburger $5.00")
listbox.insert(3, "-Drink $5.00")
listbox.insert(4, "-Pene  $5.00")

# asda

def create_option_panel():
    new_window = Toplevel()
    new_window.geometry("200x200")
    Button(new_window, text="Create New Food", command=create_food_panel).pack(pady=20)
    Button(new_window, text="Create New Drink", command=create_food_panel).pack(pady=20)


def create_food_panel():
    new_window = Toplevel()
    new_window.geometry("300x600")
    label_name = Label(new_window, text="Name:")
    entry_name = Entry(new_window, borderwidth=0, highlightthickness=0, background="#463239", fg="white",
                       justify="center")

    label_calories = Label(new_window, text="Calories:")
    entry_calories = Entry(new_window, borderwidth=0, highlightthickness=0, background="#463239",
                           fg="white", justify="center")

    label_price = Label(new_window, text="Price:")
    entry_price = Entry(new_window, borderwidth=0, highlightthickness=0, background="#463239", fg="white",
                        justify="center")

    label_price = Label(new_window, text="Price:")
    entry_price = Entry(new_window, borderwidth=0, highlightthickness=0, background="#463239", fg="white",
                        justify="center")

    label_ingredientes = Label(new_window, text="Ingredients:")
    entry_ingredientes = Entry(new_window, borderwidth=0, highlightthickness=0, background="#463239",
                               fg="white", justify="center")

    label_description = Label(new_window, text="Description:")
    entry_description = Entry(new_window, borderwidth=0, highlightthickness=0, background="#463239",
                              fg="white", justify="center")

    label_Amount = Label(new_window, text="Amount:")
    entry_Amount = Entry(new_window, borderwidth=0, highlightthickness=0, background="#463239",
                         fg="white", justify="center")

    label_name.pack()
    entry_name.pack()

    label_calories.pack()
    entry_calories.pack()

    label_price.pack()
    entry_price.pack()

    label_ingredientes.pack()
    entry_ingredientes.pack()

    label_description.pack()
    entry_description.pack()

    label_Amount.pack()
    entry_Amount.pack()
    # label.grid(row = 0 , column=0,columnspan=5)
    # entry.grid(row = 1 , column=1,columnspan=5 )


Button(window, text="Create...", command=create_option_panel).pack()

window.mainloop()
