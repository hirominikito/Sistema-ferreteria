# main.py

from db_manager import crear_base_datos, instertar_producto_prueba, mostrar_base_datos,buscar_producto

if __name__ == "__main__":
    print("Iniciando sistema de gestion ferreteria..")
    
    crear_base_datos()
    # codigo_proovedor, proveedor_origen, nombre, precio_costo, stock_actual, porcentaje_ganancia
    instertar_producto_prueba("19283","Bulonera Sur S.A","Tornillo Fix 40x6",15.0,500,100)
    instertar_producto_prueba("19277","Bulonera Sur S.A","Tornillo Fix 50x5",17.0,500,100)
    instertar_producto_prueba("122-9002","Herrajes Covelli","Bisagra Mariposa 20x50",725.0,20,100)
    instertar_producto_prueba("090-2134","Herrajes Covelli","Picaporte bce simple",5678.0,5,80)
    instertar_producto_prueba("8293","El Taladro","Martillo Carpintero 300",4321.0,5,70)
    instertar_producto_prueba("8256","El Taladro","Alicate 9",6234.0,5,70)
    mostrar_base_datos()
    busqueda = str(input())
    buscar_producto(busqueda)
    