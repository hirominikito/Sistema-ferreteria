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
        precio_costo REAL,
        porcentaje_ganancia REAL DEFAULT 40.0,
        stock_actual INTEGER DEFAULT 0,
        stock_minimo INTEGER DEFAULT 5
    )
                   """)
    conexion.commit()
    conexion.close()

    print("BD y tabla creados con exito")

def instertar_producto_prueba(codigo,proveedor,nombre,costo,ganancia,stock):
    conexion = sqlite3.connect("ferreteria.db")
    cursor = conexion.cursor()
    
    sql = """
        INSERT INTO productos  (codigo_proveedor,proveedor_origen,nombre,precio_costo,porcentaje_ganancia,stock_actual)
        VALUES (?,?,?,?,?,?)
    """
    cursor.execute(sql,(codigo,proveedor,nombre,costo,ganancia,stock))
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

