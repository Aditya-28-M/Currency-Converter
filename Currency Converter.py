# Import CurrencyConverter from the currency_converter package and tkinter for GUI
from currency_converter import CurrencyConverter
import tkinter as tk

# Create an instance of the CurrencyConverter class
c = CurrencyConverter()

# Initialize the main application window
window = tk.Tk()
window.geometry("600x400")  # Set window size
window.title("Currency Converter")  # Set window title

# Function that handles the conversion when the button is clicked
def clicked():
    amount = float(entry1.get())            # Get the amount entered by the user
    cur1 = entry2.get().upper()             # Get source currency and convert to uppercase
    cur2 = entry3.get().upper()             # Get target currency and convert to uppercase
    data = c.convert(amount, cur1, cur2)    # Convert the currency
    # Display the result in a new label
    tk.Label(window, text=data, font="Times 16 bold").place(x=200, y=300)


# Heading label for the GUI
tk.Label(window, text="Currency Converter", font="Times 25 bold").place(x=150, y=40)

# Label and Entry for amount input
tk.Label(window, text="Enter amount here: ", font="Times 14 bold").place(x=120, y=100)
entry1 = tk.Entry(window)

# Label and Entry for source currency
tk.Label(window, text="Enter your current currency: ", font="Times 14 bold").place(x=40, y=150)
entry2 = tk.Entry(window)

# Label and Entry for target currency
tk.Label(window, text="Enter your converting currency: ", font="Times 14 bold").place(x=15, y=200)
entry3 = tk.Entry(window)

# Button to trigger the conversion
tk.Button(window, text="Convert", font="Times 16 bold", command=clicked).place(x=250, y=270)

# Positioning the entry fields in the window
entry1.place(x=290, y=105)
entry2.place(x=290, y=155)
entry3.place(x=290, y=205)

# Start the GUI event loop
window.mainloop()





