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
        technical_cost = int(float(technical_cost_entry.get()))
        logystics = float(logystics_cost_entry.get())
        seller_commission = cost * DEFAULT_VALUES["DEFAULT_COMMISSION"]
        owner_commission = cost * DEFAULT_VALUES["OWNER_COMMISSION"]
        
        cost_before_taxes = cost + technical_cost + logystics
        total_cost = cost_before_taxes + seller_commission + owner_commission + (cost_before_taxes * DEFAULT_VALUES["TAXES"]) + (cost_before_taxes * DEFAULT_VALUES["RENTABILITY"]) + (cost_before_taxes * DEFAULT_VALUES["STRUCTURE"])
        
        ideal_price = total_cost * 1.2
        
        if ideal_price*DEFAULT_VALUES["RENTABILITY"] < total_cost:
            ideal_price = total_cost * 2
        
        print(f"Precio de venta mínimo sugerido: {ideal_price:,.2f}\n")
                
        
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
    technical_cost_label = tk.Label(query_frame, text="Costo del técnico instrumentador")
    logystics_cost_label = tk.Label(query_frame, text="Logística")
    
    product_label.grid(row=0, column=0)
    cost_label.grid(row=1, column=0)
    technical_cost_label.grid(row=2, column=0)
    logystics_cost_label.grid(row=3, column=0)
    
    # Inputs
    product_entry = ttk.Combobox(query_frame, width=27, values=LISTA_ARTICULOS) 
    cost_entry = ttk.Entry(query_frame, width=30)
    technical_cost_entry = ttk.Entry(query_frame, width=30)
    logystics_cost_entry = ttk.Entry(query_frame, width=30)
    calculate_button = ttk.Button(query_frame, text="Calcular", command=calculate)
    
    product_entry.grid(row=0, column=1)
    cost_entry.grid(row=1, column=1)
    technical_cost_entry.grid(row=2, column=1)
    logystics_cost_entry.grid(row=3, column=1)
    calculate_button.grid(row=4, column=0, columnspan=2)
    
    # update cost input when choosing a product from combobox
    
    default_product = LISTA_ARTICULOS[0] if LISTA_ARTICULOS else None
    if default_product:
        product_entry.set(default_product)
        update_cost(None)
    
    product_entry.bind("<<ComboboxSelected>>", update_cost)
    
    for widget in query_frame.winfo_children():
        widget.grid_configure(padx=5, pady=10)
        
    window.mainloop()


if __name__ == '__main__':
    main()