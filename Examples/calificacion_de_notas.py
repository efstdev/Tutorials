# Estamos buscando cual fue la nota finale del estudiante
# Ex; A, B, C, D, F

# Para empezar necesitamos la nota del estudiante (0 a 100)

nota = int(input("Tu nota: "))
# En ese input escribes lo que diga en la seccion de esperado
# Me refiero al "Cual fue tu nota?", "Cual es tu nota?", eso

# Primero.. hay que poner un error si se escribe que la nota es  <0 o >100

if nota == nota < 0 or nota > 100: # <-- nota < menor que zero o nota > mayor que 100
    print("error") 
#Esto da un error si el estudiante pone algo menor a 0 o mayor de 100


# Ese input ahora tenemos que ver si es de cierta cantidad a otra. 
# Esta parte se hace con if y elif (else if), en ORDEN
if nota == 100 or nota >= 90:
    print("Esto da A")

elif nota == 80 or nota >= 89: # Arregle esto que puse 80 y 80 en de vez de 80 y 89
    print("Esto da B")

elif nota == 70 or nota >= 79:
    print("Esto da C")


# Con esto puedes hacer el resto :3
#Good luck




