# Evitando duplicacion en tu codigo [ ESPANOL ]

# IFs, ELIFs, ELSEs
#
# Vamos a suponer que estamos realizando comparaciones de numeros.
# Si el input es menor que 5, asignar un valor; si es mayor, asignar otro

# Ejemplo #1
__INPUT__ = input()
# NO
if __INPUT__ > 5:            
    x = "Greater than 5"
elif __INPUT__ < 5:
    x = "Less than 5"

# SI
if __INPUT__> 5:
    x = "Greater than 5"
else:
    x = "Less than 5"

# En comparaciones es bastante simple no repetir ni realizar
# lineas innecesarias como aqui evitamos tener que definir un elif,
# ya que esperamos tan solo un numero mayor o menor.
#
# El 'if' compara el input a ver si es mayor, si no es mayor entonces
# continua con las proximas lineas
#
# Utilizando 'elif' se utiliza mas bien cuando tenemos 
# posibilades distintas de inputs
#
# Si tenemos que comparar si es "a" o "b" es inneficiente utilizar
# "elif" ya que tienes que definir la condicion



# Ejemplo #2
__INPUT__ = input()
# NO
if __INPUT__ == 'a':
    print('a')
if __INPUT__ == 'b':
    print('b')
if __INPUT__ == 'c':
    print('c')
if __INPUT__ != 'a' and __INPUT__ != 'b' and __INPUT__ != 'c':
    print('none')

# SI
if __INPUT__ == 'a':
    print('a')
elif __INPUT__ == 'b':
    print('b')
elif __INPUT__ == 'c':
    print('c')
else: 
    print('none')

# Que se hizo aqui? Cual es la differencia entre el NO y SI?
# Bueno, si utilizamos el fragmento de arriba el definir tantos "if"
# puede conllevar a ciertos problemas en programas mas extensos,
# pero como asi? En este caso no es haci,
# si en tu programa de alguna forma se cumplen mas de un if, entonces se ejecutan
# por que funcionan independiente de uno al otro
# 
# If + Elifs + Else, funcionan dependiente al otro en orden escrito.
# Si no se cumple uno, pues continua con el siguiente
#
# Si estamos verificando a ver si el input *NO* es igual a lo que queremos
# no es necesario escribir un 'if' o 'elif' con varios != ya que 'else' hace eso por ti.
# El 'else' basicamente dice que si NINGUNO anterior es cumple pues se ejecuta el.
# Como ni el 'if' ni los 'elifs' se cumplen, significa que el input no es ninguno de los
# valores que queremos asi que ponemos un 'else' para deshacer mas eficientemente de inputs 
# no deseados
#
# Mas adelante las repeticiones en codigos se vuelven obsoletas cuando entremos a def()