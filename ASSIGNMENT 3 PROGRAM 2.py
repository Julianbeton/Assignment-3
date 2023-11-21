import tkinter as tk
from tkinter import messagebox

def calculate_total_quantity_and_change():
    try:
        amount_of_money = float(amount_of_money_entry.get())
        apple_price_per_piece = float(apple_price_per_piece_entry.get())

        total_quantity_of_apple = amount_of_money // apple_price_per_piece
        change = ((amount_of_money / apple_price_per_piece) - total_quantity_of_apple) * apple_price_per_piece
        offer = total_quantity_of_apple + 1

        total_quantity_of_apple_result = f"Quantity of Apple🍎:  {total_quantity_of_apple} Apples"
        apple_price_per_piece_result = f"Apple🍎 Price:  ₱{apple_price_per_piece}"
        amount_of_money_result = f"Amount of Money you have:  ₱{amount_of_money}"
        change_result = f"Change:  ₱{change}"
        offer_result = f"NOTE: Make an offer to the Vendor \nto make it {offer} pieces so she/he don't\nhave to give you any Change."

        output_window = tk.Toplevel()
        output_window.title("Total Quantity of Apple")
        output_window.geometry("450x250")
        output_window.configure(bg="#800000")

        total_quantity_of_apple_result_label = tk.Label(output_window, text=total_quantity_of_apple_result, fg="#76EE00", bg="#800000", font=("Times", "18", "bold italic"))
        total_quantity_of_apple_result_label.pack()

        apple_price_per_piece_result_label = tk.Label(output_window, text=apple_price_per_piece_result, fg="#FF6347", bg="#800000", font=("Times", "18", "bold italic"))
        apple_price_per_piece_result_label.pack()

        amount_of_money_result_label = tk.Label(output_window, text=amount_of_money_result, fg="#FF6347", bg="#800000", font=("Times", "19", "bold italic"))
        amount_of_money_result_label.pack()

        change_result_label = tk.Label(output_window, text=change_result, fg="#FF6347", bg="#800000", font=("Times", "19", "bold italic"))
        change_result_label.pack()

        offer_result_label = tk.Label(output_window, text=offer_result, fg="#FF6347", bg="#800000", font=("Times", "19", "bold italic"))
        offer_result_label.pack()

    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid number.")

window = tk.Tk()
window.title("Apple App Calculator")
window.configure(bg="#FF6347")
window.geometry("490x220")     

label = tk.Label(window, text=" Apple🍎App Calculator                            ", font=("Times", "36","bold italic"), bg="#FF6347", fg="#76EE00").grid(row=0, column=0, sticky=tk.W)

tk.Label(window, text = "           Amount of Money:", font=("Helvetica", "20", "bold italic"), bg="#FF6347", fg="#800000").grid(row=1, column=0, sticky=tk.W)
amount_of_money_entry = tk.Entry(window, width=10, font=("Times", "20", "bold italic"),bg="#800000",fg="#76EE00")
amount_of_money_entry.grid(row = 1, column = 0, pady = 5) 

tk.Label(window, text = " Apple🍎 Price Per Piece:", font=("Helvetica", "20", "bold italic"), bg="#FF6347", fg="#800000").grid(row=2, column=0, sticky=tk.W)
apple_price_per_piece_entry = tk.Entry(window, width=10, font=("Times", "20", "bold italic"),bg="#800000",fg="#76EE00")
apple_price_per_piece_entry.grid(row = 2, column = 0, pady = 5)

calculate_button = tk.Button(window, text="Calculate", command=calculate_total_quantity_and_change, width=8, height=1, font=("Times", "18","bold italic"), bg="#76EE00", fg="#800000", padx=15, pady=5)
calculate_button.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()