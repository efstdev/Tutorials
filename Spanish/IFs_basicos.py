# Conditions [If, elif, else]

# Los Ifs, funcionan en conjunto a los booleans,
# Si el boolean propuesto en el If es cierto, entonces el codigo de adentro se ejecuta
# Esto puede ser con numeros, variables

if True:     #SIEMPRE tienen que acompañado de los dos puntitos :
  print("This is a True boolean") # Lo que esta adentro debe ir indentado con 2 espacios o 4 espacios

if 3 > 1:
  print("This is a True comparison")

if 5 > 20:
  print("Will not print") # Este no va a imprimir nada, ya que nuestro If es falso.

#Usando variables
a = 2
b = 6
c = 'UPR'
d = 'UPRM'

if a > b:
  print("This will not print") # Este no imprime nada por que a (2) no es mayor que b (6)

if c != d:
  print("This is True") # Esto imprime por que nuestra comparasion es cierta, c no es igual a d

if c == 'UPR':
  print("This is true")

if d == 2:
  print("This will not print")


# A las condiciones y comparators se les puede añadir otros operadores como: not, and, or
#Aqui se pone tricky, pero nada tan complicado

if 2 == 2 and 5 == 5:
  print("This is True")
  # Cuando utilizas 'and', ambos lados deben estar True para que el If se cumpla

if 2 == 4 and 2 == 2:
  print("This will not print")
  # Esto no imprime por que solo UN lado es True

if 2 == 2 or 5 == 3:
  print("This will print") # Esto imprime por que cuando utulizamos 'or'
                        # Tan solo un lado de la operacion tienen que esta cierta para que se cumpla

if 2 == 5 or 7 == 4:
  print("This will not print") # Ambos lados son False, lo que invalida la operacion y no imprime

# Tambien como cualquier otra, podemos utilizar variables
e = 4
f = 8
g = 'RUM'
h = 'Portico'

if e != f and g == 'RUM': # Aqui este imprime por que e (4) no es igual a f (8), 
  print('This will print')  #Y por que g (RUM) si es igual a RUM   

#Vamos a complicarlo un poco con multiples and y or
if h == 'Portico' or (3 == 3 and e != f):
  print('''This is True,
        Aqui podemos ver el uso de dos comparaciones "or" y "and" 
        La comparacion de h es True, por que h si es igual a Portico
        Ahora miramos al segundo lado donde tenemos otra comparacion en parentesis
        comparamos a ver si 3 es igual a 3, lo cual es cierto y si e no es igual a f, lo cual es cierto''')

if (g == 'RUM' and h == "Portico") and (e < f or 7 < 3):
    print("These will print")
    # Aqui estamos usando parentesis para dividir nuestras comparaciones, eso se conoce como Precedence, al igual que en matematicas
    # Los parentesis tienen prioridad sobre las demas cosas. Lo que significa que primero se hace lo que esta adentro y luego lo de afuera.
    # En este caso primero se verifica si g es RUM y h es Portico, y si e es menor que f o si 7 es menor que 3 antes de comparar una con la otra
    # Nuestra primera comparacion es Cierta ya que g si es igual a RUM y h si es igual a Portico

    # En nuestro segunda comparacion tenemor un 'or', que tan solo un lado debe estar correcto para que sea True
    # Tenemos a ver si e es menor que o si 7 es menor que 3, como una de ellas es cierta (e < f, que es 4 < 8) pues toda nuestra
    # Comparacion se vuelve cierta, ahora podemos visualisarlo de otra manera
    # Podemos verla asi 
if True and True: print() # Como ambos lados son True, nuestro IF se cumple y ejecuta el codigo dentro