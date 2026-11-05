


# Tipos de operadores en Python


#operadores aritmeticos
a = 10
b = 3

suma = a + b

resta = a - b

multiplicacion = a * b

division = a / b

exponente = a ** b

raiz_cuadrada = a ** 0.5

modulo = a % b # el modulo devuelve el resto de la division

#operadores logicos

x = True
y = False


# Operador AND dvuelve True solo si ambos valores son true, cualquier otro caso devuelve False
# este Y este
and_result = x and y
print(and_result)

# Operador OR devuelve True si almenos uno de los valores es True 
# este O este
or_result = x or y
print(or_result)

# Operador NOT devuelve el valor contrario al que se le conmpara
# que NO sea este
not_result = not y
print(not_result)


#Operadores de comparacion

a = 5
b = 10

tupla_operadores_comparacion = (
    # Igual que
    a == b, # devuelve True si a es igual a b
    
    # diferente que
    a != b, # devuelve True si a es diferente a b
    
    # menor que
    a < b, # devuelve True si a es menor que b
    
    # mayor que
    a > b, # devuelve True si a es mayor que b
    
    # menor o igual que
    a <= b, # devuelve True si a es menor o igual que b
    
    # mayor o igual que
    a >= b # devuelve True si a es mayor o igual que b
)
for i in tupla_operadores_comparacion:
    print(i)

# Operadores de asignacion

# Asignacion simple 
c = 5   
# Asignacion con operadores aritmeticos
# simplifica la escritura de las operaciones aritmeticas y asigna el resultado a la variable
c += 2 # c = c + 2
c -= 3 # c = c - 3          
c *= 4 # c = c * 4
c /= 2 # c = c / 2
c **= 3 # c = c ** 3
c %= 2 # c = c % 2
c //= 2 # c = c // 2

# Operadores de identidad Sirve para comparar los valores de dos objetos y determinar si son el mismo objeto en memoria. 

numero1 = -6
numero1 += 1
#numero = int(input("Ingrese un número: "))
mi_otro_numero = -5
print('mi_numero:',numero1, 'mi_otro_numero:', mi_otro_numero)
print(numero1 is mi_otro_numero) # devuelve True si ambos objetos son el mismo objeto en memoria
print(numero1 is not mi_otro_numero) # devuelve True si ambos objetos no son el mismo objeto en memoria

'''
Existe algo muy curioso en la comparacion de numeros en el espacio de la memoria en python, por defecto python crea una cache de objetos
para los numeros enteros entre -5 y 256, esto significa que si se crean dos variables con el mismo valor dentro de este rango de enteros
ambas variables apuntaran al mismo objeto en memoria, por lo que la comparacion de identidad devolvera True.

esto no funciona con los flotantes ya que no se puede hacer una cache de objetos flotantes debido a que hay un numero infinito de decimales,
entonces python calcula o guarda cada numero flotante como un objeto independiente, por lo que la comparacion de identidad devolvera False.

'''
#Operadores de pertenencia Sirve para determinar si un valor se encuentra dentro de una secuencia (como una lista, tupla o cadena de texto)

lista = [1, 2, 3, 4, 5]
print(3 in lista) # devuelve True si el valor 3 se encuentra en la lista
print(6 not in lista) # devuelve True si el valor 6 no se encuentra en  la lista        

hola = 'Hola'
print ('H' in hola) # devuelve True si el valor 'H' se encuentra en la cadena de texto
print('a' not in hola) # devuelve True si el valor 'a' no se encuentra en la cadena de texto    

tupla = (1, 2, 3, 4, 5)
print(3 in tupla) # devuelve True si el valor 3 se encuentra en la tupla
print(6 not in tupla) # devuelve True si el valor 6 no se encuentra en la tupla

#operadores bit a bit Sirve para realizar operaciones a nivel de bits en números enteros. Los operadores bit a bit trabajan con la representación binaria de los números.

a = 10 # 1010
b = 3 # 0011

print(f"AND: 10 & 3 = {a & b}") # AND bit a bit, d   evuelve 2 (0010)
print(f"OR: 10 | 3 = {a | b}") # OR bit a bit, devuelve 11 (1011)
print(f"XOR: 10 ^ 3 = {a ^ b}") # XOR bit a bit, devuelve 9 (1001)
print(f"NOT: ~10 = {~a}") # NOT bit a bit, devuelve -11 (inverso de 10 en binario)
print(f"Left Shift: 10 << 1 = {a << 1}") # Desplazamiento a la izquierda, devuelve 20 (10100)
print(f"Right Shift: 10 >> 1 = {a >> 1}") # Desplazamiento a la derecha, devuelve 5 (0101)