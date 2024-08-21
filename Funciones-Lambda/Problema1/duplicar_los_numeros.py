def problema1():
  numeros = [1, 2, 3, 4, 5]

  # Usando lambda para duplicar los números
  duplicados = list(map(lambda x: x * 2, numeros))

  print(duplicados)  # [2, 4, 6, 8, 10]


if __name__ == "__main__":
  problema1()
