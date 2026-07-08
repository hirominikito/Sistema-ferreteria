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


