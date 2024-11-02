import tkinter as tk
from tkinter import ttk
from consts import *

# Log de usuario
def log(text):
    print(text)

# Verificar credenciales
def verify_credentials(username, password):
    # Convertir a minúsculas lo que el usuario ingrese para la comparacion
    username = username.lower()
    password = password.lower()

    if USUARIOS.get(username) == None:
        return False
    if USUARIOS.get(username) == password:
        return True


def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if verify_credentials(username, password):
        log("Inicio de sesión exitoso.")
        login_window.destroy()  # Cierra la ventana de inicio de sesión
        main()  # Llama a la función principal
    else:
        log("Credenciales incorrectas.")
        error_label.config(text="Credenciales incorrectas. Intenta de nuevo.")

def create_login_window():
    global username_entry, password_entry, error_label, login_window

    login_window = tk.Tk()
    login_window.title("Inicio de Sesión")
    login_window.geometry("400x300")

    tk.Label(login_window, text="Usuario:").pack(pady=5)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Contraseña:").pack(pady=5)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack(pady=5)

    tk.Button(login_window, text="Iniciar Sesión", command=login).pack(pady=20)

    error_label = tk.Label(login_window, text="", fg="red")
    error_label.pack(pady=5)

    login_window.mainloop()

def main():
    def upload_clients():
        LISTA_CLIENTES = []

        clientes = open("archivos/clientes.csv", "r", encoding="utf-8")
        lineas = clientes.read()
        renglones = lineas.split("\n")
        for renglon in renglones:
            cliente = renglon.split(",")
            LISTA_CLIENTES.append(cliente)
        clientes.close()
        for cliente in LISTA_CLIENTES:
            cliente[1] = float(cliente[1])
        return LISTA_CLIENTES
    
    CLIENTS = upload_clients()

    commision_calc = lambda cost, percent: cost * percent
    filtered_clients = list(filter(lambda client: client[1] == 0.21, CLIENTS))

    
    
    commision_calc = lambda cost, percent: cost * percent
    filtered_clients = list(filter(lambda client: client[1] == 0.21, CLIENTS))
    
    def filter_clients():
        if tax_exempt_var.get():
            filtered_clients = list(filter(lambda client: client[1] == 0, CLIENTS))
        else:
            filtered_clients = list(filter(lambda client: client[1] == 0.21, CLIENTS)) 
        tax_exempt_entry['values'] = [client[0] for client in filtered_clients]    
        
   
    def update_cost(event=None):
        product = product_entry.get()
        cost = ARTICULOS.get(product, 0.0)
        cost_entry.delete(0, tk.END)
        cost_entry.insert(0, f"{cost}")
   
    def calculate(event=None):
        try:
            cost = int(float(cost_entry.get()))
            technical_cost = int(float(technical_cost_entry.get()))
            logystics = float(logystics_cost_entry.get())
            seller_commission = commision_calc(cost, DEFAULT_VALUES[0][1])
            owner_commission = commision_calc(cost, DEFAULT_VALUES[1][1])
        
            cost_before_taxes = cost + technical_cost + logystics
            total_cost = cost_before_taxes + seller_commission + owner_commission + (cost_before_taxes * DEFAULT_VALUES[2][1]) + (cost_before_taxes * DEFAULT_VALUES[3][1]) + (cost_before_taxes * DEFAULT_VALUES[4][1])
        
            ideal_price = total_cost * 1.2
        
            if ideal_price*DEFAULT_VALUES[3][1] < total_cost:
                ideal_price = total_cost * 1.6463
    
            result_entry.delete(0, tk.END)
            result_entry.insert(0, f"{ideal_price:,.2f}")

            price_with_IVA= ideal_price*(1+float(iva_entry.get()))
            Resul_iva_entry.delete(0, tk.END)
            Resul_iva_entry.insert(0, f"{price_with_IVA:,.2f}")
            

        
            print(f"Precio de venta mínimo sugerido: {ideal_price:,.2f}\n")

            
        except ValueError:
            print(f"Error: valor inválido {ValueError}")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Error: valor inválido")
        except Exception:
            print(f"Error: {Exception}")
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Error: cálculo fallido")


    def update_iva(event=None):
        client = tax_exempt_entry.get()
        tax_exempt_entry.delete(0, tk.END)
        tax_exempt_entry.insert(0, f"{client}")
        iva_entry.insert(0, f"{list(filter(lambda cl: cl[0] == client, CLIENTS))[0][1]}")



       
    window = tk.Tk()
    window.title("Cotizadora de ventas")
   
    main_frame = tk.Frame(window)
    main_frame.pack()
   
    # Inputs to query the price of the product
    query_frame = tk.LabelFrame(main_frame, text="Información del producto")
    query_frame.grid(row=0, column=0, padx=20, pady=20)
   
    # Labels
    product_label = tk.Label(query_frame, text="Producto")
    tax_exempt_entry = tk.Label(query_frame, text="Clientes")
    cost_label = tk.Label(query_frame, text="Costo del producto")
    technical_cost_label = tk.Label(query_frame, text="Costo del técnico instrumentador")
    logystics_cost_label = tk.Label(query_frame, text="Logística")
    result_label = tk.Label(query_frame, text="Precio mínimo de venta ideal")
    iva_label = tk.Label(query_frame, text="IVA")
    Resul_iva=tk.Label(query_frame, text="Precio ideal con IVA")
   
    product_label.grid(row=0, column=0)
    tax_exempt_entry.grid(row=1, column=0)
    cost_label.grid(row=2, column=0)
    technical_cost_label.grid(row=3, column=0)
    logystics_cost_label.grid(row=4, column=0)
    result_label.grid(row=6, column=0,)
    iva_label.grid(row=7, column=0)
    Resul_iva.grid(row=8, column=0)
   
    # Inputs
    tax_exempt_var = tk.BooleanVar() # Booleano para el checkbox
    
    product_entry = ttk.Combobox(query_frame, width=27, values=LISTA_ARTICULOS)
    cost_entry = ttk.Entry(query_frame, width=30)
    technical_cost_entry = ttk.Entry(query_frame, width=30)
    logystics_cost_entry = ttk.Entry(query_frame, width=30)
    calculate_button = ttk.Button(query_frame, text="Calcular", command=calculate)
    result_entry = ttk.Entry(query_frame, width=30)
    tax_exempt_entry = ttk.Combobox(query_frame, width=27, values=[client[0] for client in filtered_clients])
    tax_exempt_check = tk.Checkbutton(query_frame, variable=tax_exempt_var, text='Exentos IVA', onvalue=1, offvalue=0, command=filter_clients)
    iva_entry = ttk.Entry(query_frame, width=30)
    Resul_iva_entry = ttk.Entry(query_frame, width=30)
   
    product_entry.grid(row=0, column=1)
    tax_exempt_entry.grid(row=1, column=1)
    tax_exempt_check.grid(row=1, column=2)
    cost_entry.grid(row=2, column=1)
    technical_cost_entry.grid(row=3, column=1)
    logystics_cost_entry.grid(row=4, column=1)
    calculate_button.grid(row=5, column=0, columnspan=3)
    result_entry.grid(row=6, column=1)
    iva_entry.grid(row=7, column=1)
    Resul_iva_entry.grid(row=8, column=1)
       
    # update cost input when choosing a product from combobox
   
    default_product = LISTA_ARTICULOS[0] if LISTA_ARTICULOS else None
    if default_product:
        product_entry.set(default_product)
        update_cost(None)
   
    product_entry.bind("<<ComboboxSelected>>", update_cost)
    calculate_button.bind("<Button-1>", calculate)

    tax_exempt_entry.bind("<<ComboboxSelected>>", update_iva)
   
    for widget in query_frame.winfo_children():
        widget.grid_configure(padx=5, pady=10)
       
    window.mainloop()
 
 
if __name__ == '__main__':
    create_login_window()

    