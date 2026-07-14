# main.py

from db_manager import crear_base_datos, instertar_producto_prueba, mostrar_base_datos,buscar_producto

if __name__ == "__main__":
    print("Iniciando sistema de gestion ferreteria..")
    
    crear_base_datos()
    # codigo_proovedor, proveedor_origen, nombre, precio_costo, stock_actual, porcentaje_ganancia
    # instertar_producto_prueba("15253","Bulonera Sur S.A","Clavo 1' x kg",3250.0,5,100)
    # instertar_producto_prueba("15244","Bulonera Sur S.A","Clavo 2' x kg",2850.0,5,100)
    # instertar_producto_prueba("122-9002","Herrajes Covelli","Cerradura larga ang",5666.0,4,100)
    # instertar_producto_prueba("090-2134","Herrajes Covelli","Piton 6 c/t cerrado",127.0,100,100)
    instertar_producto_prueba("8293","El Taladro","Amoladora 800w",51001.0,2,40)
    instertar_producto_prueba("8256","El Taladro","Agujereadora 600w",61234.0,2,40)
    mostrar_base_datos()
    busqueda = str(input())
    buscar_producto(busqueda)
    