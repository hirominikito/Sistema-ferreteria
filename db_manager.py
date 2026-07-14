# db_manager.py

import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("ferreteria.db")
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
    conexion.commit()
    conexion.close()

    print("BD y tabla creados con exito")

def instertar_producto_prueba(codigo,proveedor,nombre,costo,stock,ganancia):
    conexion = sqlite3.connect("ferreteria.db")
    cursor = conexion.cursor()
    
    sql = """
        INSERT INTO productos  (codigo_proveedor,proveedor_origen,nombre,precio_costo,stock_actual,porcentaje_ganancia)
        VALUES (?,?,?,?,?,?)
    """
    cursor.execute(sql,(codigo,proveedor,nombre,costo,stock,ganancia))
    conexion.commit()
    conexion.close()
    print(f"Se agrego el producto: '{nombre}' a la base de datos")
    
def mostrar_base_datos():
    conexion = sqlite3.connect("ferreteria.db")
    cursor = conexion.cursor()
    
    sql = "SELECT * FROM productos"
    cursor.execute(sql)
    filas = cursor.fetchall()

    for fila in filas:
        print(fila)
    conexion.close()
    print("hola")
    
def buscar_producto(busqueda):
    conexion = sqlite3.connect("ferreteria.db")
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
    conexion.close()
    return productos

def actualizar_stock(id_producto_a_modificar,cantidad_a_agregar):
    conexion = sqlite3.connect("ferreteria.db")
    cursor = conexion.cursor()
    
    sql = """
        UPDATE productos
        SET stock_actual = stock_actual + ?
        WHERE id = ?
    """
    cursor.execute(sql,(cantidad_a_agregar,id_producto_a_modificar))
    conexion.commit()
    conexion.close()
    print(f"Base de datos actualizada, ID: {id_producto_a_modificar} sumo: {cantidad_a_agregar} unidades")
    

    
    
