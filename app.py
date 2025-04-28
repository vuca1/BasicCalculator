import tkinter as tk


def main():

    # Initialize the Tkinter GUI
    window = tk.Tk()
    window.title("Calculator desu")
    window.geometry("230x200")
    window.resizable(False, False)

    # main label / label
    entry_box = tk.Entry(window, width=30)
    entry_box.grid(row=0, column=0, columnspan=4 ,padx= 20 ,pady=10)

    # config the main label
    def change_label(num):
        entry_box.insert(tk.END, str(num))

    #grid
    buttons = [
        ("1", 1, 0),
        ("2", 1, 1),
        ("3", 1, 2),
        ("4", 2, 0),
        ("5", 2, 1),
        ("6", 2, 2),
        ("7", 3, 0),
        ("8", 3, 1),
        ("9", 3, 2),
        ("+", 1, 3),
        ("-", 2, 3),
        ("*", 3, 3),
        ("/", 4, 3)
    ]

    # number buttons - creates all buttons from 1 to 10(9)
    for (text, row, col) in buttons:
        num_button = tk.Button(window, text=text, command=lambda num=text: change_label(num))
        num_button.grid(row=row ,column=col, padx=3, pady=3)

    # calculate function
    def calculate():
        entry_box.delete(0, tk.END) # set 'entry_box' empty
        entry_box.insert(0, "calculating...")

    # equals button
    equals_button = tk.Button(window, text="=", command=calculate)
    equals_button.grid(row=4, column=2, padx=3, pady=3)


    window.mainloop()

if __name__ == "__main__":
    main()