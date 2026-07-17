# db_manager.py

import sqlite3

def crear_base_datos():
    with sqlite3.connect("ferreteria.db") as conexion:
        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo_proveedor TEXT,
            proveedor_origen TEXT,
            nombre TEXT NOT NULL,
            stock_actual INTEGER DEFAULT 0,
            precio_costo REAL,
            precio_venta REAL GENERATED ALWAYS AS (precio_costo*((porcentaje_ganancia/100)+1)),
            porcentaje_ganancia REAL DEFAULT 40.0,
            stock_minimo INTEGER DEFAULT 5
        )
                       """)
        print("BD y tabla creados con exito")

def insertar_producto_prueba(codigo,proveedor,nombre,costo,stock,ganancia):
    with sqlite3.connect("ferreteria.db") as conexion:
        cursor = conexion.cursor()

        sql = """
            INSERT INTO productos  (codigo_proveedor,proveedor_origen,nombre,precio_costo,stock_actual,porcentaje_ganancia)
            VALUES (?,?,?,?,?,?)
        """
        cursor.execute(sql,(codigo,proveedor,nombre,costo,stock,ganancia))
        print(f"Se agrego el producto: '{nombre}' a la base de datos")
        conexion.commit()
    
def mostrar_base_datos():
    with sqlite3.connect("ferreteria.db") as conexion:
        cursor = conexion.cursor()

        sql = "SELECT * FROM productos"
        cursor.execute(sql)
        filas = cursor.fetchall()

        for fila in filas:
            print(fila)

    
def buscar_producto(busqueda):
    with sqlite3.connect("ferreteria.db") as conexion:
        cursor = conexion.cursor()
        sql = """
            SELECT * FROM productos
            WHERE codigo_proveedor LIKE ? OR nombre LIKE ?
        """
        comodin = f"%{busqueda}%"
        cursor.execute(sql,(comodin,comodin))
        productos = cursor.fetchall()
        for producto in productos:
            print(producto)
        return productos

def actualizar_stock(id_producto_a_modificar,cantidad_a_agregar):
    with sqlite3.connect("ferreteria.db") as conexion:
        cursor = conexion.cursor()

        sql = """
            UPDATE productos
            SET stock_actual = stock_actual + ?
            WHERE id = ?
        """
        cursor.execute(sql,(cantidad_a_agregar,id_producto_a_modificar))
        print(f"Base de datos actualizada, ID: {id_producto_a_modificar} sumo: {cantidad_a_agregar} unidades")
    
def insertar_nuevo_producto(cod_proveedor,nombre_proveedor,nombre_producto,costo,ganancia,stock,stock_minimo):
    with sqlite3.connect("ferreteria.db") as conexion:
        cursor = conexion.cursor()
        sql = """
            INSERT INTO productos (codigo_proveedor,proveedor_origen,nombre,precio_costo,porcentaje_ganancia,stock_actual,stock_minimo)  
            VALUES (?,?,?,?,?,?,?)      
        """
        cursor.execute(sql,(cod_proveedor,nombre_proveedor,nombre_producto,costo,ganancia,stock,stock_minimo))
        conexion.commit()


    
    
