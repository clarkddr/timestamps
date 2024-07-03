def actualizar_con_anterior(lista_diccionarios, clave):
    valor_anterior = None                               # Al principio no tenemos valor, se inicializa
    for diccionario in lista_diccionarios:              # Se hace la iteracion
        valor_actual = diccionario[clave]               # Se le asigna a la variable el valor actual
        if valor_anterior is not None:                  # se condiciona a que si el valor no es None, aplica el codigo que esta dentro. Esto quita que se aplique la iteracion sobre el primer elemento
            diccionario[clave] = valor_anterior         # Se aplica el nuevo valor
        valor_anterior = valor_actual                   # Se le asigna a valor anterior el valor actual para usarlo en la siguiente iteracion


lista_diccionarios = [
    {'nombre': 'Juan', 'edad': 25},
    {'nombre': 'María', 'edad': 30},
    {'nombre': 'Pedro', 'edad': 40},
    {'nombre': 'Ana', 'edad': 35},
    {'nombre': 'Maleny', 'edad': 29},
    {'nombre': 'Itzayana', 'edad': 7},
    {'nombre': 'David', 'edad': 4}
]

actualizar_con_anterior(lista_diccionarios, 'nombre')

for diccionario in lista_diccionarios:
    print(diccionario)
