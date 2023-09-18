import mysql.connector

# Configura la conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ariketa1"
)
if(conexion != None):
    print("Conexion a la base de datos correcta")
else:
    print("Conexion erronea")
# Crea un cursor
cursor = conexion.cursor()

# Ejecuta consultas SQL o realiza operaciones en la base de datos aquí



# ... (código de conexión previo)

# Función para introducir un nombre en la base de datos
def introducir_nombre(cursor):
    nombre = input("Introduce un nombre: ")
    # Insertar el nombre en la base de datos
    consulta = "INSERT INTO erabiltzailea (Nombre) VALUES (%s)"
    datos = (nombre,)
    cursor.execute(consulta, datos)
    conexion.commit()
    print(f"{nombre} ha sido añadido correctamente.")

# Función para mostrar todos los nombres en la base de datos
def mostrar_nombres(cursor):
    # Recuperar todos los nombres de la base de datos
    cursor.execute("SELECT Nombre FROM erabiltzailea")
    nombres = cursor.fetchall()
    if nombres:
        print("Nombres almacenados:")
        for nombre in nombres:
            print(nombre[0])
    else:
        print("No hay nombres almacenados.")

# Función para editar un nombre en la base de datos
def editar_nombre(cursor):
    nombre_a_editar = input("Introduce el nombre que quieres editar: ")
    nuevo_nombre = input("Introduce el nuevo nombre: ")
    # Actualizar el nombre en la base de datos
    consulta = "UPDATE erabiltzailea SET Nombre = %s WHERE nombre = %s"
    datos = (nuevo_nombre, nombre_a_editar)
    cursor.execute(consulta, datos)
    conexion.commit()
    print(f"{nombre_a_editar} ha sido editado a {nuevo_nombre}.")

# Función para eliminar un nombre de la base de datos
def eliminar_nombre(cursor):
    nombre_a_eliminar = input("Introduce el nombre que quieres eliminar: ")
    # Eliminar el nombre de la base de datos
    consulta = "DELETE FROM erabiltzailea WHERE nombre = %s"
    datos = (nombre_a_eliminar,)
    cursor.execute(consulta, datos)
    conexion.commit()
    print(f"{nombre_a_eliminar} ha sido eliminado correctamente.")



# Menú principal
while True:
    print("\nMenú:")
    print("1. Introducir nombre")
    print("2. Mostrar todos los nombres")
    print("3. Editar un nombre")
    print("4. Eliminar un nombre")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        introducir_nombre(cursor)
    elif opcion == "2":
        mostrar_nombres(cursor)
    elif opcion == "3":
        editar_nombre(cursor)
    elif opcion == "4":
        eliminar_nombre(cursor)
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Introduce un número del 1 al 5.")

# Fin del programa
print("Cerrando el programa")

# Cierra el cursor y la conexión cuando hayas terminado
cursor.close()
conexion.close()