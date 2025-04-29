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

    def add_brackets():
        global equation
        equation = str(equation)
        if equation == "":
            add_to_equation("(")
        else:
            last_char = equation[-1]
            if last_char == "(":
                delete_last()
                add_to_equation(")")
            elif last_char == ")":
                delete_last()
                add_to_equation("(")
            elif last_char != "(" and last_char != ")":
                add_to_equation("(")


    # round number
    def round_number():
        global equation
        try:
            equation = float(equation)
            equation = round(equation)
            change_label(equation)
        except Exception as e:
            change_label("Not a number - press Erase")

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
            (" 1 ", 1, 0, "1"),
            (" 2 ", 1, 1, "2"),
            (" 3 ", 1, 2, "3"),
            (" 4 ", 2, 0, "4"),
            (" 5 ", 2, 1, "5"),
            (" 6 ", 2, 2, "6"),
            (" 7 ", 3, 0, "7"),
            (" 8 ", 3, 1, "8"),
            (" 9 ", 3, 2, "9")
        ]

    # number buttons - creates all buttons from 1 to 10(9)
    for (text, row, col, text2) in buttons:
            num_button = tk.Button(window, text=text, command=lambda num=text2: add_to_equation(num))
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

    # round button
    round_button = tk.Button(window, text="Round", command=round_number)
    round_button.grid(row=5, column=0, padx=3, pady=3)

    # erase button
    erase_button = tk.Button(window, text="Erase", command=lambda: change_label(""))
    erase_button.grid(row=5, column=2, padx=3, pady=3)

    # decimal button
    decimal_button = tk.Button(window, text=" . ", command=lambda: add_to_equation("."))
    decimal_button.grid(row=4, column=2, padx=3, pady=3)

    # brackets button
    bracket_button = tk.Button(window, text="()", command=add_brackets)
    bracket_button.grid(row=4, column=0, padx=3, pady=3)

    window.mainloop()

if __name__ == "__main__":
    main()