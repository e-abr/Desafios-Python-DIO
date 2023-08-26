numPedidos = int(input())

for i in range(1, numPedidos + 1):
  prato = input()
  calorias = int(input())
  ehVegano = input()

  if ehVegano == "s":
      ehVeganoTexto = "Vegano"
  else:
      ehVeganoTexto = "Nao-vegano"

  print(f"Pedido {i}: {prato} ({ehVeganoTexto}) - {calorias} calorias")




#//TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.
