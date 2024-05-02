import pyodbc
import tkinter 
from tkinter import messagebox

# Función para conectar a la base de datos
def conectar():
    try:
        conexion = pyodbc.connect(
            'DRIVER={SQL Server};'
            'SERVER=JEISSON-AREVALO;'
            'DATABASE=Personal;'
            'Trusted_Connection=yes;'
        )
        return conexion
    except pyodbc.Error as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
        return None

# Función para insertar un nuevo registro en la base de datos
def insertar_registro(nombre, apellido, fecha_nacimiento, telefono, email, cargo, salario):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            consulta = "INSERT INTO PersonalActivo (Nombre, Apellido, FechaNacimiento, Telefono, Email, Cargo, Salario) VALUES (?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(consulta, (nombre, apellido, fecha_nacimiento, telefono, email, cargo, salario))
            conexion.commit()
            messagebox.showinfo("Registro Insertado", "El nuevo registro se ha insertado correctamente.")
            cursor.close()
            conexion.close()
    except pyodbc.Error as e:
        messagebox.showerror("Error al insertar", f"No se pudo insertar el registro: {e}")

# Función para actualizar un registro en la base de datos
def actualizar_registro(id, nombre, apellido, fecha_nacimiento, telefono, email, cargo, salario):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            consulta = "UPDATE PersonalActivo SET Nombre=?, Apellido=?, FechaNacimiento=?, Telefono=?, Email=?, Cargo=?, Salario=? WHERE PersonaID=?"
            cursor.execute(consulta, (nombre, apellido, fecha_nacimiento, telefono, email, cargo, salario, id))
            conexion.commit()
            messagebox.showinfo("Registro Actualizado", "El registro se ha actualizado correctamente.")
            cursor.close()
            conexion.close()
    except pyodbc.Error as e:
        messagebox.showerror("Error al actualizar", f"No se pudo actualizar el registro: {e}")

# Función para eliminar un registro de la base de datos
def eliminar_registro(id):
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            consulta = "DELETE FROM PersonalActivo WHERE PersonaID=?"
            cursor.execute(consulta, (id,))
            conexion.commit()
            messagebox.showinfo("Registro Eliminado", "El registro se ha eliminado correctamente.")
            cursor.close()
            conexion.close()
    except pyodbc.Error as e:
        messagebox.showerror("Error al eliminar", f"No se pudo eliminar el registro: {e}")

# Función para mostrar todos los registros de la base de datos
def mostrar_registros():
    try:
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM PersonalActivo")
            registros = cursor.fetchall()
            cursor.close()
            conexion.close()
            return registros
    except pyodbc.Error as e:
        messagebox.showerror("Error al leer", f"No se pudieron obtener los registros: {e}")
        return []

# Función para manejar el evento de botón "Insertar"
def insertar_registro_Interfaz():
    # Obtener valores de las entradas
    nombre = Nombre.get()
    apellido = Apellido.get()
    fecha_nacimiento = FechaNacimiento.get()
    telefono = Telefono.get()
    email = Email.get()
    cargo = Cargo.get()
    salario = Salario.get()

    # Insertar el nuevo registro
    insertar_registro(nombre, apellido, fecha_nacimiento, telefono, email, cargo, salario)

# Función para manejar el evento de botón "Actualizar"
def actualizar_registro_interfaz():
    # Obtener valores de las entradas
    id = Id.get()
    nombre = Nombre.get()
    apellido = Apellido.get()
    fecha_nacimiento = FechaNacimiento.get()
    telefono = Telefono.get()
    email = Email.get()
    cargo = Cargo.get()
    salario = Salario.get()

    # Actualizar el registro con el id especificado
    actualizar_registro(id, nombre, apellido, fecha_nacimiento, telefono, email, cargo, salario)

# Función para manejar el evento de botón "Eliminar"
def eliminar_registro_interfaz():
    # Obtener el id del registro a eliminar
    id = Id.get()

    # Eliminar el registro con el id especificado
    eliminar_registro(id)

# Función para mostrar todos los registros en la consola
def mostrar_registros_interfaz():
    registros = mostrar_registros()
    if registros:
        for registro in registros:
            print(registro)
    else:
        print("No se encontraron registros.")

# Crear la ventana principal
ventana = tkinter.Tk()
ventana.geometry("600x500")

# Crear campos de entrada (Entry) para cada dato
tkinter.Label(ventana, text="ID:").pack()
Id = tkinter.Entry(ventana)
Id.pack()

tkinter.Label(ventana, text="Nombre:").pack()
Nombre = tkinter.Entry(ventana)
Nombre.pack()

tkinter.Label(ventana, text="Apellido:").pack()
Apellido = tkinter.Entry(ventana)
Apellido.pack()

tkinter.Label(ventana, text="Fecha de Nacimiento:").pack()
FechaNacimiento = tkinter.Entry(ventana)
FechaNacimiento.pack()

tkinter.Label(ventana, text="Teléfono:").pack()
Telefono = tkinter.Entry(ventana)
Telefono.pack()

tkinter.Label(ventana, text="Email:").pack()
Email = tkinter.Entry(ventana)
Email.pack()

tkinter.Label(ventana, text="Cargo:").pack()
Cargo = tkinter.Entry(ventana)
Cargo.pack()

tkinter.Label(ventana, text="Salario:").pack()
Salario = tkinter.Entry(ventana)
Salario.pack()

# Botones para realizar operaciones CRUD
tkinter.Button(ventana, text="Insertar Registro", command=insertar_registro).pack()
tkinter.Button(ventana, text="Actualizar Registro", command=actualizar_registro_interfaz).pack()
tkinter.Button(ventana, text="Eliminar Registro", command=eliminar_registro_interfaz).pack()
tkinter.Button(ventana, text="Mostrar Registros", command=mostrar_registros_interfaz).pack()

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()
