from tkinter import *

window = Tk()
window.geometry("400x600")
window.configure(bg= "#645853")
listbox = Listbox(window , bg="#645853", font=("Arial" , 35 , ) , foreground="white", width=20)
listbox.pack()
listbox.insert(1 , "-Pizza $5.00")
listbox.insert(2 , "-Hamburger $5.00")
listbox.insert(3 , "-Drink $5.00")
listbox.insert(4 , "-Pene  $5.00")

#asda
def create_option_panel():
    new_window = Toplevel()
    new_window.geometry("200x200")
    Button(new_window , text = "Create New Food", command = create_food_panel).pack(pady=20)
    Button(new_window , text = "Create New Drink", command = create_food_panel).pack(pady=20)

def create_food_panel():
    new_window = Toplevel()
    new_window.geometry("300x600")
    Entry(new_window , borderwidth=0,highlightthickness=0 , background="#463239").pack(pady=20)

Button(window , text = "Create...", command = create_option_panel).pack()



window.mainloop()