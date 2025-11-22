import tkinter as tk
from tkinter import ttk, messagebox
from math import factorial


def permutacion(n):
    
    return factorial(n)

def combinatoria(n, k):
    if k > n or n < 0 or k < 0:
        raise ValueError("Valores inválidos: asegura 0 <= k <= n.")
    return factorial(n) // (factorial(k) * factorial(n - k))

def combinacion_con_repeticion(n, k):
    if n <= 0 or k < 0:
        raise ValueError("Valores inválidos: n>0 y k>=0.")
    return factorial(n + k - 1) // (factorial(k) * factorial(n - 1))

def permutacion_con_repeticion(n, lista_repeticiones):
    
    denom = 1
    for r in lista_repeticiones:
        if r < 0:
            raise ValueError("Repeticiones negativas no válidas.")
        denom *= factorial(r)
    return factorial(n) // denom

def variacion_sin_repeticion(n, k):
    if k > n or n < 0 or k < 0:
        raise ValueError("Valores inválidos: asegura 0 <= k <= n.")
    return factorial(n) // factorial(n - k)

def variacion_con_repeticion(n, k):
    if n < 0 or k < 0:
        raise ValueError("Valores inválidos: n>=0 y k>=0.")
    return n ** k

def numero_multinomial(n, lista_k):
    denom = 1
    for k in lista_k:
        if k < 0:
            raise ValueError("Componentes del vector multinomial no pueden ser negativas.")
        denom *= factorial(k)
    return factorial(n) // denom


def parse_int(s):
    s = s.strip()
    if s == "":
        raise ValueError("Campo vacío.")
    return int(s)

def parse_list_of_ints(s):
    
    if not s.strip():
        raise ValueError("Lista vacía.")
    sep = ',' if ',' in s else None
    raw = s.split(',') if sep else s.split()
    nums = [int(x.strip()) for x in raw if x.strip() != ""]
    if not nums:
        raise ValueError("Lista inválida.")
    return nums


class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculadora Combinatoria")
        root.resizable(True,True)
        padding = {'padx': 8, 'pady': 6}

      
        self.oper_var = tk.StringVar(value="Permutación")
        self.n_var = tk.StringVar()
        self.k_var = tk.StringVar()
        self.lista_var = tk.StringVar()
        self.result_var = tk.StringVar(value="Resultado: ")

     
        ttk.Label(root, text="Operación:").grid(row=0, column=0, sticky="w", **padding)
        self.combo = ttk.Combobox(root, textvariable=self.oper_var, state="readonly", width=30)
        self.combo['values'] = [
            "Permutación",
            "Permutación con repetidos",
            "Combinación",
            "Combinación con repetición",
            "Variación",
            "Variación con repetición",
            "Número Multinomial"
        ]
        self.combo.grid(row=0, column=1, columnspan=2, sticky="ew", **padding)
        self.combo.bind("<<ComboboxSelected>>", self.on_operacion_change)

       
        ttk.Label(root, text="n:").grid(row=1, column=0, sticky="w", **padding)
        self.entry_n = ttk.Entry(root, textvariable=self.n_var)
        self.entry_n.grid(row=1, column=1, columnspan=2, sticky="ew", **padding)

     
        ttk.Label(root, text="k:").grid(row=2, column=0, sticky="w", **padding)
        self.entry_k = ttk.Entry(root, textvariable=self.k_var)
        self.entry_k.grid(row=2, column=1, columnspan=2, sticky="ew", **padding)

        
        ttk.Label(root, text="Lista (ej: 2,2,1):").grid(row=3, column=0, sticky="w", **padding)
        self.entry_lista = ttk.Entry(root, textvariable=self.lista_var)
        self.entry_lista.grid(row=3, column=1, columnspan=2, sticky="ew", **padding)

     
        self.btn_calc = ttk.Button(root, text="Calcular", command=self.calcular)
        self.btn_calc.grid(row=4, column=0, **padding)

        self.btn_limpiar = ttk.Button(root, text="Limpiar", command=self.limpiar)
        self.btn_limpiar.grid(row=4, column=1, **padding)

        self.btn_salir = ttk.Button(root, text="Salir", command=root.quit)
        self.btn_salir.grid(row=4, column=2, **padding)

  
        self.label_res = ttk.Label(root, textvariable=self.result_var, font=("Segoe UI", 11))
        self.label_res.grid(row=5, column=0, columnspan=3, sticky="w", **padding)

        
        self.on_operacion_change()

    def on_operacion_change(self, event=None):
       
        op = self.oper_var.get()

        
        self.entry_n.config(state="normal")
        self.entry_k.config(state="normal")
        self.entry_lista.config(state="normal")

        if op == "Permutación":
            self.entry_k.config(state="disabled")
            self.entry_lista.config(state="disabled")
        elif op == "Permutación con repetidos":
            self.entry_k.config(state="disabled")
            self.entry_lista.config(state="normal")
        elif op == "Combinación":
            self.entry_k.config(state="normal")
            self.entry_lista.config(state="disabled")
        elif op == "Combinación con repetición":
            self.entry_k.config(state="normal")
            self.entry_lista.config(state="disabled")
        elif op == "Variación":
            self.entry_k.config(state="normal")
            self.entry_lista.config(state="disabled")
        elif op == "Variación con repetición":
            self.entry_k.config(state="normal")
            self.entry_lista.config(state="disabled")
        elif op == "Número Multinomial":
            self.entry_k.config(state="disabled")
            self.entry_lista.config(state="normal")

    def calcular(self):
        op = self.oper_var.get()
        try:
            
            if op == "Permutación":
                n = parse_int(self.n_var.get())
                res = permutacion(n)

            elif op == "Permutación con repetidos":
                n = parse_int(self.n_var.get())
                lista = parse_list_of_ints(self.lista_var.get())
               
                if sum(lista) != n:
                   
                    if not messagebox.askyesno("Confirmar", "La suma de las repeticiones no coincide con n. ¿Deseas continuar?"):
                        return
                res = permutacion_con_repeticion(n, lista)

            elif op == "Combinación":
                n = parse_int(self.n_var.get())
                k = parse_int(self.k_var.get())
                res = combinatoria(n, k)

            elif op == "Combinación con repetición":
                n = parse_int(self.n_var.get())
                k = parse_int(self.k_var.get())
                res = combinacion_con_repeticion(n, k)

            elif op == "Variación":
                n = parse_int(self.n_var.get())
                k = parse_int(self.k_var.get())
                res = variacion_sin_repeticion(n, k)

            elif op == "Variación con repetición":
                n = parse_int(self.n_var.get())
                k = parse_int(self.k_var.get())
                res = variacion_con_repeticion(n, k)

            elif op == "Número Multinomial":
                n = parse_int(self.n_var.get())
                lista = parse_list_of_ints(self.lista_var.get())
               
                if sum(lista) != n:
                    if not messagebox.askyesno("Confirmar", "La suma de los k no coincide con n. ¿Deseas continuar?"):
                        return
                res = numero_multinomial(n, lista)

            else:
                raise ValueError("Operación desconocida")

            self.result_var.set(f"Resultado: {res}")

        except ValueError as ve:
            messagebox.showerror("Error de entrada", str(ve))
        except Exception as e:
           
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def limpiar(self):
        self.n_var.set("")
        self.k_var.set("")
        self.lista_var.set("")
        self.result_var.set("Resultado: ")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
