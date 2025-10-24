lis = [1, 2, 3, 4, 5]
def invert_lista(lista: list) -> list:
     if len(lista) == 2:
          return [lista[1], lista[0]]
     return invert_lista(lista[1::]) + [lista[0]]

print(invert_lista(lis))