import tkinter as tk
from tkinter import messagebox

def calculate_total_amount():
    try:
        apple_quantity = int(apple_quantity_entry.get())
        orange_quantity = int(orange_quantity_entry.get())
        amount_of_money = int(amount_of_money_entry.get())

        apple_price_per_piece = 20
        orange_price_per_piece = 25

        total_amount = (apple_quantity * apple_price_per_piece) + (orange_quantity * orange_price_per_piece)
        change = amount_of_money - total_amount

        amount_of_money_result = f"Amount of Money you have:     {amount_of_money} Pesos"
        total_amount_to_pay = f"    Total Amount to Pay:     -{total_amount} Pesos"
        change_result = f"        Your Change =     {change} Pesos"

        output_window = tk.Toplevel()
        output_window.title("Amount of Money - Total Amount to Pay = Change")
        output_window.geometry("450x120")
        output_window.configure(bg="#FF6347")

        amount_of_money_label = tk.Label(output_window, text=amount_of_money_result, fg="#76EE00", bg="#FF6347", font=("Times", "18", "bold italic"))
        amount_of_money_label.pack()

        total_amount_label = tk.Label(output_window, text=total_amount_to_pay, fg="#76EE00", bg="#FF6347", font=("Times", "18", "bold italic"))
        total_amount_label.pack()

        change_label = tk.Label(output_window, text=change_result, fg="#76EE00", bg="#FF6347", font=("Times", "19", "bold italic"))
        change_label.pack()

    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid number.")

window = tk.Tk()
window.title("Apple and Orange Suppliers")
window.configure(bg="#FF6347")
window.geometry("480x320")     

label = tk.Label(window, text=" Apple🍎 and Orange🍊                           \nSuppliers                          ", font=("Times", "36","bold italic"), bg="#FF6347", fg="#76EE00").grid(row=0, column=0, sticky=tk.W)

tk.Label(window, text = "  Apple Quantity🍎(₱20):", font=("Helvetica", "20", "bold italic"), bg="#FF6347", fg="#800000").grid(row=1, column=0, sticky=tk.W)
apple_quantity_entry = tk.Entry(window, width=10, font=("Times", "20", "bold italic"),bg="#800000",fg="#76EE00")
apple_quantity_entry.grid(row = 1, column = 0, pady = 5)

tk.Label(window, text = "Orange Quantity🍊(₱25):", font=("Helvetica", "20", "bold italic"), bg="#FF6347", fg="#800000").grid(row=2, column=0, sticky=tk.W)
orange_quantity_entry = tk.Entry(window, width=10, font=("Times", "20", "bold italic"),bg="#800000",fg="#76EE00")
orange_quantity_entry.grid(row = 2, column = 0, pady = 5)

tk.Label(window, text = "          Amount of Money:", font=("Helvetica", "20", "bold italic"), bg="#FF6347", fg="#800000").grid(row=3, column=0, sticky=tk.W)
amount_of_money_entry = tk.Entry(window, width=10, font=("Times", "20", "bold italic"),bg="#800000",fg="#76EE00")
amount_of_money_entry.grid(row = 3, column = 0, pady = 5)

calculate_button = tk.Button(window, text="Calculate", command=calculate_total_amount, width=8, height=1, font=("Times", "18","bold italic"), bg="#76EE00", fg="#800000", padx=15, pady=5)
calculate_button.grid(row=8, column=0, columnspan=2, pady=5)

window.mainloop()