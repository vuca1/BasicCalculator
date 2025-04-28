import time
import tkinter as tk

def main():
    global equation
    equation = ""

    # Initialize the Tkinter GUI
    window = tk.Tk()
    window.title("Calculator desu")
    window.geometry("230x200")
    window.resizable(False, False)

    # main label / entry
    entry_box = tk.Entry(window, width=30)
    entry_box.grid(row=0, column=0, columnspan=4 ,padx= 20 ,pady=10)

    # adds something to the equation string
    def add_to_equation(value):
        global equation
        equation = str(equation)
        equation += str(value)
        entry_box.delete(0, tk.END)
        entry_box.insert(0, equation)

    # remove the entry_box and put a new value to it
    def change_label(value):
        global equation
        equation = value
        value = str(value)
        entry_box.delete(0, tk.END)
        entry_box.insert(0, value)

    # delete last character from 'entry_box'
    def delete_last():
        global equation
        equation = str(equation)
        equation = equation[:-1]
        change_label(equation)

    # calculate function
    def calculate():
        global equation
        try:
            equation = eval(equation)
            change_label(equation)
        except Exception as e:
            change_label(f"Error - {e}")
            time.sleep(2)
            change_label("")


    # grid
    buttons = [
            (" 1 ", 1, 0),
            (" 2 ", 1, 1),
            (" 3 ", 1, 2),
            (" 4 ", 2, 0),
            (" 5 ", 2, 1),
            (" 6 ", 2, 2),
            (" 7 ", 3, 0),
            (" 8 ", 3, 1),
            (" 9 ", 3, 2)
        ]

    # number buttons - creates all buttons from 1 to 10(9)
    for (text, row, col) in buttons:
            num_button = tk.Button(window, text=text, command=lambda num=text: add_to_equation(num))
            num_button.grid(row=row, column=col, padx=3, pady=3)

    # zero button
    zero_button = tk.Button(window, text=" 0 ", command=lambda: add_to_equation("0"))
    zero_button.grid(row=4, column=1, padx=3, pady=3)

    # minus button
    minus_button = tk.Button(window, text=" - ", command=lambda: add_to_equation("-"))
    minus_button.grid(row=2, column=3, padx=3, pady=3)

    # plus button
    plus_button = tk.Button(window, text=" + ", command=lambda: add_to_equation("+"))
    plus_button.grid(row=1, column=3, padx=3, pady=3)

    # divide button
    divide_button = tk.Button(window, text=" / ", command=lambda: add_to_equation("/"))
    divide_button.grid(row=3, column=3, padx=3, pady=3)

    # multiply button
    multiply_button = tk.Button(window, text=" * ", command=lambda: add_to_equation("*"))
    multiply_button.grid(row=4, column=3, padx=3, pady=3)

    # equals button
    equals_button = tk.Button(window, text="  =  ", command=calculate)
    equals_button.grid(row=5, column=3, padx=3, pady=3)

    # back / delete button
    back_button = tk.Button(window, text="Back", command=delete_last)
    back_button.grid(row=5, column=1, padx=3, pady=3)

    # erase button
    erase_button = tk.Button(window, text="Erase", command=lambda: change_label(""))
    erase_button.grid(row=5, column=2, padx=3, pady=3)

    # decimal button
    decimal_button = tk.Button(window, text=" . ", command=lambda: add_to_equation("."))
    decimal_button.grid(row=4, column=2, padx=3, pady=3)

    window.mainloop()

if __name__ == "__main__":
    main()