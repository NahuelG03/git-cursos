def agregar_cliente(lista_de_cliente,nombre,apellido,dni):
        cliente = {}
        cliente['nombre'] = nombre
        cliente['apellido'] = apellido
        cliente['dni'] = dni
        clientes.append(cliente)

def lista_clientes(clientes):
    for i in clientes:
        print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, DNI: {i['dni']}")

def mostrar_cliente(clientes,dni):
    for i in clientes:
        if i['dni'] == dni:
            print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, DNI: {i['dni']}")
            return True
    return False

def eliminar_cliente(clientes,dni):
    for i in clientes:
        if i['dni'] == dni:
            clientes.remove(i)
            return True
    return False

clientes =[]

while True:
    print("""\t.:Menú de opciones:.\n
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar cliente por DNI
4. Eliminar cliente    
5. Salir""")
    opcion = int(input("Ingrese la opción deseada: "))
    print()

    if opcion == 1:
        nombre = input("Digite el nombre: ")
        apellido = input("Digite el apellido: ")
        dni = input("Digite el D.N.I: ")
        agregar_cliente(clientes,nombre,apellido,dni)

    elif opcion == 2:
        lista_clientes(clientes)

    elif opcion == 3:
        dni = input("Digite el D.N.I: ")
        if mostrar_cliente(clientes,dni):
            print("Cliente encontrado")
        else:
            print("Cliente no encontrado")

    elif opcion == 4:
        dni = input("Digite el D.N.I: ")
        if eliminar_cliente(clientes,dni):
            print("Cliente eliminado")
        else:
            print("Cliente no encontrado")

    elif opcion == 5:
        break

    else:
        print("Error, se equivocó de opción de menú")

    print()