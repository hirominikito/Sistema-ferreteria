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
    
    tabla.tag_configure("alerta_stock", background="#ff7575")

    for producto in productos_buscados:
        stock_actual = producto[4]
        stock_minimo = producto[8]
                
        if stock_actual <= stock_minimo: 
            tabla.insert("", tk.END,values=(producto),tags=("alerta_stock",))
        else:
            tabla.insert("",tk.END, values=producto)
        
def al_seleccionar_producto(event):
    print("¡Clic detectado en la tabla!")
    seleccion = tabla.selection()
    
    if not seleccion:
        return
    
    item_id = seleccion[0]
    valores_producto = tabla.item(item_id,"values")
    precio_final = valores_producto[6]
    label_precio_gigante.config(text=f" {precio_final}")

ventana = tk.Tk()
ventana.title("Control de stock - Ferreteria")
ventana.geometry("765x450")
entrada_busqueda = tk.Entry(ventana, font=("Arial",14), width=50,)
entrada_busqueda.grid(row=0,column=0,padx=10,pady=10)
entrada_busqueda.bind("<KeyRelease>",lambda event: actualizar_tabla())

boton_busqueda = tk.Button(ventana, text="Buscar", font=("Arial",11), command=lambda: actualizar_tabla())
boton_busqueda.grid(row=0,column=1,padx=10,pady=10)

columnas = ("id", "codigo", "proveedor", "nombre", "costo", "stock","precio_venta")
tabla = ttk.Treeview(ventana, columns=columnas, show="headings", height=15)

tabla.heading("id", text="Codigo local")
tabla.heading("codigo", text="Codigo proveedor")
tabla.heading("proveedor", text="Proveedor")
tabla.heading("nombre", text="Producto")
tabla.heading("costo", text="Prec. Costo")
tabla.heading("stock", text="Stock")
tabla.heading("precio_venta", text="Precio")


tabla.column("id", width=60, anchor="center")
tabla.column("codigo", width=110, anchor="center")
tabla.column("proveedor", width=120)
tabla.column("nombre", width=250)
tabla.column("costo", width=80, anchor="e")
tabla.column("stock", width=60, anchor="center")
tabla.column("precio_venta", width=60, anchor="e")

tabla.grid(row=1,column=0,columnspan=3,padx=10,pady=5)

titulo_precio = tk.Label(ventana, text="PRECIO DE VENTA",font=("Arial",12,"bold"))
titulo_precio.grid(row=2,column=0,pady=(20,0))
label_precio_gigante = tk.Label(ventana, text="$0.00",font=("Arial",28,"bold"),fg="green")
label_precio_gigante.grid(row=3,column=0,columnspan=4,pady=10)


actualizar_tabla()

tabla.bind("<<TreeviewSelect>>", al_seleccionar_producto)




ventana.mainloop()
