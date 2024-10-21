from os import system
import sqlite3
from sqlite3.dbapi2 import Cursor
import time

def conexion():
    conectar = sqlite3.connect('Contactos.db')
    cursor =  conectar.cursor()
    return conectar, cursor

def agregar():
    conectar, cursor = conexion()
    Nombre, Telefono, Email = str(input('Inserte su nombre, telefono y email')).split()
    datos = Nombre, Telefono, Email
    sql = """
    INSERT INTO Contactos (Nombre, Telefono, Email) VALUES (?, ?, ?)
    """
    print('Datos guardados' if cursor.execute(sql, datos) else 'No se pudieron guardar los datos')
    conectar.commit() and conectar.close

def mostrar():
    conectar, cursor = conexion()
    cursor.execute('SELECT Id, Nombre, Telefono, Email from Contactos')
    for fila in cursor:
        print(f"""ID = {fila[0]}
        Nombre = {fila[1]}
        Telefono = {fila[2]}
        Email = {fila[3]}     
        """)
        conectar.close

def buscar():
    conectar, cursor = conexion()
    Nombre = str(input('Buscar por nombre: '))
    if(len(Nombre) > 0):
        sql = "SELECT * FROM Contactos WHERE Nombre LIKE ?"
        parametros = (f'%{Nombre}%',)
        result = cursor.execute(sql,parametros)
        for data in result:
            print(f""" 
            +Id : {data[0]}
            +Nombre : {data[1]}
            +Telefono : {data[2]}
            +Email : {data[3]}
            """)
            conectar.commit()
            conectar.close()


