# interfaz.py

import tkinter as tk
from tkinter import ttk
from db_manager import buscar_producto

def actualizar_tabla():
    if tabla.get_children():
        for i in tabla.get_children():
            tabla.delete(i)
    busqueda = entrada_busqueda.get()
    productos_buscados = buscar_producto(busqueda)

    for producto in productos_buscados:
        tabla.insert("", tk.END,values=(producto))
    

ventana = tk.Tk()
ventana.title("Control de stock - Ferreteria")
ventana.geometry("700x450")
entrada_busqueda = tk.Entry(ventana, font=("Arial",14), width=30,)
entrada_busqueda.grid(row=0,column=0,padx=10,pady=10)
entrada_busqueda.bind("<KeyRelease>",lambda event: actualizar_tabla())

boton_busqueda = tk.Button(ventana, text="Buscar", font=("Arial",11), command=lambda: actualizar_tabla())
boton_busqueda.grid(row=0,column=1,padx=10,pady=10)

columnas = ("id", "codigo", "proveedor", "nombre", "costo", "stock")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=15)

tabla.heading("id", text="Codigo local")
tabla.heading("codigo", text="Codigo proveedor")
tabla.heading("proveedor", text="Proveedor")
tabla.heading("nombre", text="Producto")
tabla.heading("costo", text="Prec. Costo")
tabla.heading("stock", text="Stock")

tabla.column("id", width=60, anchor="center")
tabla.column("codigo", width=110, anchor="center")
tabla.column("proveedor", width=120)
tabla.column("nombre", width=250)
tabla.column("costo", width=80, anchor="e")
tabla.column("stock", width=60, anchor="center")

tabla.grid(row=1,column=0,columnspan=3,padx=10,pady=5)

actualizar_tabla()





ventana.mainloop()
