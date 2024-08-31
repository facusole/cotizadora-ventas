import tkinter as tk
from tkinter import ttk
from consts import *

def main():
    total = 0
    seller_commission = 0
    
    def update_cost(event):
        product = product_entry.get()
        cost = ARTICULOS.get(product, 0.0)
        cost_entry.delete(0, tk.END)
        cost_entry.insert(0, f"{cost}")
    
    def calculate():
        cost = int(float(cost_entry.get()))
        ammount = int(float(ammount_entry.get()))
        commission = float(commission_entry.get())
        
        total = ammount - cost
        seller_commission = total * commission
        
        print(f"Total: {total:,.2f}\nSeller commission: {seller_commission:,.2f}")
                
        
    window = tk.Tk()
    window.title("Cotizadora de ventas")
    
    main_frame = tk.Frame(window)
    main_frame.pack()
    
    # Inputs to query the price of the product
    query_frame = tk.LabelFrame(main_frame, text="Query information")
    query_frame.grid(row=0, column=0, padx=20, pady=20)
    
    # Labels
    product_label = tk.Label(query_frame, text="Producto")
    cost_label = tk.Label(query_frame, text="Costo del producto")
    ammount_label = tk.Label(query_frame, text="Precio de venta")
    commission_label = tk.Label(query_frame, text="Comisión del vendedor")
    
    product_label.grid(row=0, column=0)
    cost_label.grid(row=1, column=0)
    ammount_label.grid(row=2, column=0)
    commission_label.grid(row=3, column=0)
    
    # Inputs
    product_entry = ttk.Combobox(query_frame, width=27, values=LISTA_ARTICULOS) 
    cost_entry = ttk.Entry(query_frame, width=30)
    ammount_entry = ttk.Entry(query_frame, width=30)
    commission_entry = ttk.Entry(query_frame, width=30)
    calculate_button = ttk.Button(query_frame, text="Calcular", command=calculate)
    
    product_entry.grid(row=0, column=1)
    cost_entry.grid(row=1, column=1)
    ammount_entry.grid(row=2, column=1)
    commission_entry.grid(row=3, column=1)
    calculate_button.grid(row=4, column=0, columnspan=2)
    
    # update cost input when choosing a product from combobox
    
    default_product = LISTA_ARTICULOS[0] if LISTA_ARTICULOS else None
    if default_product:
        product_entry.set(default_product)
        update_cost(None)
    
    product_entry.bind("<<ComboboxSelected>>", update_cost)
    
    if DEFAULT_COMMISSION:
        commission_entry.insert(0, f"{DEFAULT_COMMISSION}")
    
    for widget in query_frame.winfo_children():
        widget.grid_configure(padx=5, pady=10)
        
    window.mainloop()


if __name__ == '__main__':
    main()