# interfaz.py

import tkinter as tk
from tkinter import ttk
from db_manager import buscar_producto, actualizar_stock, insertar_nuevo_producto
id_producto_seleccionado = 0

def actualizar_tabla():
    if tabla.get_children():
        for i in tabla.get_children():
            tabla.delete(i)
    busqueda = entrada_busqueda.get()
    productos_buscados = buscar_producto(busqueda)
    
    tabla.tag_configure("alerta_stock", background="#ff7575")

    for producto in productos_buscados:
        id_prod = producto[0]
        cod_prov = producto[1]
        prov = producto[2]
        nombre = producto[3]
        stock_actual = producto[4]
        precio_costo = producto[5]
        precio_venta = producto[6]
        stock_minimo = producto[8]

        valores_fila = (id_prod, cod_prov, prov, nombre, precio_costo, stock_actual, precio_venta)
                
        if stock_actual <= stock_minimo: 
            tabla.insert("", tk.END,values=valores_fila,tags=("alerta_stock",))
        else:
            tabla.insert("",tk.END, values=valores_fila)
        
def al_seleccionar_producto(event):
    global id_producto_seleccionado
    seleccion = tabla.selection()
    
    if not seleccion:
        return False
    
    item_id = seleccion[0]
    valores_producto = tabla.item(item_id,"values")
    precio_final = round(float(valores_producto[6]),2)
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
    
    titulo_codigo_proveedor = tk.Label(ventana_nueva, text="Cod. Proveedor",font=("Arial",11))
    titulo_codigo_proveedor.grid(row=0,column=0,padx=5,pady=5)
    entrada_codigo_proveedor = tk.Entry(ventana_nueva, font=("Arial",11),width=10)
    entrada_codigo_proveedor.grid(row=1,column=0,pady=5,padx=1)
    # cod_proveedor = entrada_codigo_proveedor.get()
    titulo_nombre_proveedor = tk.Label(ventana_nueva,text="Nombre Proveedor",font=("Arial",11))
    titulo_nombre_proveedor.grid(row=0,column=1,padx=0,pady=5)
    entrada_nombre_proveedor = tk.Entry(ventana_nueva, font=("Arial",11),width=10)
    entrada_nombre_proveedor.grid(row=1,column=1,pady=5,padx=1)
    # nombre_proveedor = entrada_nombre_proveedor.get()
    titulo_nombre_producto = tk.Label(ventana_nueva,text="Nombre producto",font=("Arial",11))
    titulo_nombre_producto.grid(row=0,column=2,padx=0,pady=5)
    entrada_nombre_producto = tk.Entry(ventana_nueva, font=("Arial",11),width=10)
    entrada_nombre_producto.grid(row=1,column=2,pady=5,padx=1)    
    # nombre_producto = entrada_nombre_producto.get()
    titulo_precio_costo = tk.Label(ventana_nueva,text="Precio costo",font=("Arial",11))
    titulo_precio_costo.grid(row=0,column=3,padx=0,pady=5)
    entrada_precio_costo = tk.Entry(ventana_nueva, font=("Arial",11),width=10)
    entrada_precio_costo.grid(row=1,column=3,pady=5,padx=1)
    # precio_costo = entrada_precio_costo.get()
    titulo_ganancia = tk.Label(ventana_nueva,text="% Ganancia",font=("Arial",11))
    titulo_ganancia.grid(row=0,column=4,padx=0,pady=5)
    entrada_ganancia = tk.Entry(ventana_nueva, font=("Arial",11),width=10)
    entrada_ganancia.grid(row=1,column=4,pady=5,padx=1)
    # ganancia = entrada_ganancia.get()
    titulo_stock = tk.Label(ventana_nueva,text="Stock",font=("Arial",11))
    titulo_stock.grid(row=0,column=5,padx=0,pady=5)
    entrada_nuevo_stock = tk.Entry(ventana_nueva, font=("Arial",11),width=10)
    entrada_nuevo_stock.grid(row=1,column=5,pady=5,padx=1)
    # stock = entrada_nuevo_stock.get()
    titulo_stock_minimo = tk.Label(ventana_nueva,text="Stock minimo",font=("Arial",11))
    titulo_stock_minimo.grid(row=0,column=6,padx=0,pady=5)
    entrada_stock_minimo = tk.Entry(ventana_nueva, font=("Arial",11),width=10)
    entrada_stock_minimo.grid(row=1,column=6,pady=5,padx=1)
    # stock_minimo = entrada_stock_minimo.get()

    boton_guardad_producto = tk.Button(ventana_nueva,text="Guardar Producto",font=("Arial",11), command=lambda: validar_y_guardar_producto(
        entrada_codigo_proveedor,
        entrada_nombre_proveedor,
        entrada_nombre_producto,
        entrada_precio_costo,
        entrada_ganancia,
        entrada_nuevo_stock,
        entrada_stock_minimo,
        ventana_nueva
    ))
    boton_guardad_producto.grid(row=2,column=1,padx=10,pady=10,columnspan=2)    
    boton_cerrar_ventana = tk.Button(ventana_nueva,text="Cerrar",font=("Arial",11), command=lambda: ventana_nueva.destroy())
    boton_cerrar_ventana.grid(row=2,column=4,padx=10,pady=10,columnspan=2)

def validar_y_guardar_producto(ent_cod,ent_prov,ent_nombre,ent_costo,ent_gan,ent_stock,ent_stock_min,ventana_cerrar):
    cod_proveedor = ent_cod.get()
    nombre_proveedor = ent_prov.get()
    nombre_producto = ent_nombre.get()
    costo = ent_costo.get()
    ganancia = ent_gan.get()
    stock = ent_stock.get()
    stock_minimo = ent_stock_min.get()
    if cod_proveedor == "":
        cod_proveedor = "---"
    if nombre_proveedor == "":
        print("No se puede cargar producto sin cargar proveedor")
        return 
    if nombre_producto == "":
        print("No se puede cargar producto sin cargar nombre")
        return 
    if costo == "":
        print("No se puede cargar producto sin cargar costo")
        return 
    if ganancia == "":
        ganancia = 40
    if stock == "":
        print("No se puede guardar producto sin cargar stock")
        return 
    if stock_minimo == "":
        stock_minimo = 5
    try:
        # Intentamos guardar en la BD convirtiendo a los tipos correctos
        insertar_nuevo_producto(
            str(cod_proveedor),
            str(nombre_proveedor),
            str(nombre_producto),
            float(costo),
            float(ganancia),
            int(stock),
            int(stock_minimo)
        )
        actualizar_tabla()
        ventana_cerrar.destroy()
    except ValueError:
        print("Error: Verifica que Costo, Ganancia y Stock sean números válidos.")

ventana = tk.Tk()
ventana.title("Control de stock - Ferreteria")
ventana.geometry("765x530")

entrada_busqueda = tk.Entry(ventana, font=("Arial",14), width=40)
entrada_busqueda.grid(row=0,column=0,padx=10,pady=10)
entrada_busqueda.bind("<KeyRelease>",lambda event: actualizar_tabla())

boton_busqueda = tk.Button(ventana, text="Buscar", font=("Arial",11), command=lambda: actualizar_tabla())
boton_busqueda.grid(row=0,column=1,padx=10,pady=10)

# AGREGAR STOCK

titulo_precio = tk.Label(ventana, text="PRECIO DE VENTA",font=("Arial",12,"bold"))
titulo_precio.grid(row=2,column=0,padx=5,pady=5)

label_precio_gigante = tk.Label(ventana, text="$0.00",font=("Arial",28,"bold"),fg="green")
label_precio_gigante.grid(row=3,column=0,padx=5,pady=5)

titulo_producto = tk.Label(ventana, text="",font=("Arial",10,"bold"))
titulo_producto.grid(row=2,column=1,pady=5,padx=5)

entrada_stock = tk.Entry(ventana, font=("Arial",14),width=10)
entrada_stock.grid(row=3,column=1,pady=10,padx=5)

boton_agregar_stock = tk.Button(ventana,text="Agregar Stock", font=("Arial",11), command=lambda:guardar_nuevo_stock())
boton_agregar_stock.grid(row=4,column=1,padx=5)

boton_agregar_producto = tk.Button(ventana,text="Agregar nuevo producto",font=("Arial",10), command=lambda:abrir_ventana_producto_nuevo())
boton_agregar_producto.grid(row=2,column=2,padx=5)



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


tabla.bind("<<TreeviewSelect>>", al_seleccionar_producto)

tabla.bind("<Double-1>", al_doble_click)

actualizar_tabla()





ventana.mainloop()
