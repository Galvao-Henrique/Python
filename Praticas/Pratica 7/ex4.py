def conta_letra(letra, palavra, con=0):
     if len(palavra) == 0:
          return con
     if palavra[0] == letra:
          return conta_letra(letra, palavra[1::], con+1)
     return conta_letra(letra, palavra[1::], con)

print(conta_letra("a", "banana"))