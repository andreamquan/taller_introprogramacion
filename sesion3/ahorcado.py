print("BIENVENIDO A EL JUEGO DE AHORCADO")
nombre = input("Ingresa tu nombre: ")
print("Hola ", nombre, "!\n")


palabra = 'PRUEBA'
print("Ya hemos elegido la palabra, tiene", len(palabra), " letras")
print("Hora de adivinarla!\n")

#  o
# /|\
#  |
# / \

letra = input("Ingrese letra: ").upper()

if letra in palabra:
    print("Adivinaste! la letra se encuentra en la palabra\n")
else :
    print("La letra no esta en la palabra :(  \n")
