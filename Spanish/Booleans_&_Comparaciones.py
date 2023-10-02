# Booleans and Comparators and Conditions

#Comparators
#   Comparators basicamente comparan
#LISTA DE COMPARATORS
# < menor que     <= menor o igual que
# > mayor que     >= mayor o igual que
# == igual a      != no igual a

#OJO con =, == y !=, cuando utilizas tan solo un =
#Estas solamente dandole valor a una variable, no estas comparando.

#Cuando comparas, esto te dara a un Boolean [ True / False ]

#ejemplos:
print(5 < 2) # = False, 5 no es menor que 2
print(2 <= 2) # = True, aunque 2 no es menor que 2, si es igual a 2
print(3 > 1) # = True por que 3 si es mayor que 1
print(3 == 2) # = False por que 3 no es igual a 2
print(5 != 3) # = True por que 5 no es igual a 3

#Esto no tan solo sirve con numeros pero tambien con strings()
#para strings solo puedes usar == y !=
#ya que los otros son exclusivo a numeros
print("UPR" == "UPR") # = True por que el primer string UPR es lo mismo que el segundo UPR
print("Python" != "Javascript") # = True por que el string de Python no es lo mismo que el otro
print("UPR" == "UPRM") # = False por que el string de UPR no es igual al de UPRM

# Simple verdad?
# Los comparators se pueden utilizar tambien con variables
note = "# are used to put notes in your code"
number_a = 4   # Otra variable
number_b = 1    # Otra variable
print(note == number_a) # False note no es lo mismo que grade
print(number_a > number_b) # True number_a es mayor que number_b
