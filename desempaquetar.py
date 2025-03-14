#Desempaqueta correctamente la lista de números. 
#Crea las siguientes variables:
#"a" que debe contener el primer número, 
#"b" el último
#"c"  todos los números intermedios, como una lista
#Imprime los resultados y los datos previos.

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
a = numeros[0]
b = numeros[7]  
c = numeros[1:-1]  
print(f"a: {a}")
print(f"b: {b}")
print(f"c: {c}")
print("Desempaquetar:", *c) 