lista_numeros = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5]


def reducir_lista(lista):
    lista1 = list(set(lista))
    valor_maximo = max(lista1)
    indice_maximo = lista1.index(valor_maximo)
    lista1.pop(indice_maximo)
    return lista1
    
    
def promedio(lista):
    promedio = sum(lista) / len(lista)
    return promedio


resultado = promedio(reducir_lista(lista_numeros))
print(resultado)