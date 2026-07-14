# interfaz.py

import tkinter as tk
from tkinter import ttk
from db_manager import buscar_producto, actualizar_stock
id_producto_seleccionado = 0

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
    global id_producto_seleccionado
    seleccion = tabla.selection()
    
    if not seleccion:
        return False
    
    item_id = seleccion[0]
    valores_producto = tabla.item(item_id,"values")
    precio_final = valores_producto[6]
    label_precio_gigante.config(text=f" {precio_final}")
    titulo_producto.config(text="")
    id_producto_seleccionado = 0
    
def al_doble_click(event):
    global id_producto_seleccionado
    item_id = tabla.identify_row(event.y)

    if item_id:
        valores_producto = tabla.item(item_id,"values")
        id_producto_seleccionado = int(valores_producto[0])
        producto = valores_producto[3]
        titulo_producto.config(text=f"{producto}")
    else:    
        titulo_producto.config(text="")
        id_producto_seleccionado = 0
        
def guardar_nuevo_stock():
    global id_producto_seleccionado
    if id_producto_seleccionado == 0:
        print("Debes hacer doble click en un producto para actualizar stock!")
        return
    cantidad_a_sumar = int(entrada_stock.get())
    actualizar_stock(id_producto_seleccionado,cantidad_a_sumar)
    entrada_stock.delete(0,tk.END)
    titulo_producto.config(text="Stock actualizado!")
    id_producto_seleccionado = 0
    actualizar_tabla()
    
def abrir_ventana_producto_nuevo():
    ventana_nueva = tk.Toplevel(ventana)
    ventana_nueva.title("AGREGAR PRODUCTO NUEVO")
    ventana_nueva.geometry("765x400")

    boton_cerrar_ventana = tk.Button(ventana_nueva,text="Cerrar",font=("Arial",11), command=lambda: ventana_nueva.destroy())
    boton_cerrar_ventana.grid(row=0,column=3,padx=10,pady=10)

    

ventana = tk.Tk()
ventana.title("Control de stock - Ferreteria")
ventana.geometry("765x530")

entrada_busqueda = tk.Entry(ventana, font=("Arial",14), width=40)
entrada_busqueda.grid(row=0,column=0,padx=10,pady=10)
entrada_busqueda.bind("<KeyRelease>",lambda event: actualizar_tabla())

boton_busqueda = tk.Button(ventana, text="Buscar", font=("Arial",11), command=lambda: actualizar_tabla())
boton_busqueda.grid(row=0,column=1,padx=10,pady=10)

# AGREGAR STOCK

titulo_producto = tk.Label(ventana, text="",font=("Arial",12,"bold"))
titulo_producto.grid(row=2,column=2,pady=5,padx=5)

entrada_stock = tk.Entry(ventana, font=("Arial",14),width=10)
entrada_stock.grid(row=3,column=2,pady=10,padx=5)

boton_agregar_stock = tk.Button(ventana,text="Agregar Stock", font=("Arial",11), command=lambda:guardar_nuevo_stock())
boton_agregar_stock.grid(row=4,column=2,padx=5)

boton_agregar_producto = tk.Button(ventana,text="Agregar nuevo producto",font=("Arial",11), command=lambda:abrir_ventana_producto_nuevo())
boton_agregar_producto.grid(row=2,column=0,padx=5,columnspan=1)


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
titulo_precio.grid(row=2,column=1,padx=5,pady=5)
label_precio_gigante = tk.Label(ventana, text="$0.00",font=("Arial",28,"bold"),fg="green")
label_precio_gigante.grid(row=3,column=1,columnspan=1,padx=5,pady=5)

tabla.bind("<<TreeviewSelect>>", al_seleccionar_producto)

tabla.bind("<Double-1>", al_doble_click)

actualizar_tabla()





ventana.mainloop()
