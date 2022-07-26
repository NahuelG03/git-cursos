# hacer un programa que pida la anchura y altura de un rectangulo y con ayuda de una funcion lo dibuje con *

def dibujar(ancho,altura):
    for i in range(altura):
        for j in range(ancho):
            print("* ", end="")
        print()

ancho = int(input("Digite el ancho: "))
altura = int(input("Digite la altura: "))

print()
dibujar(ancho,altura)
