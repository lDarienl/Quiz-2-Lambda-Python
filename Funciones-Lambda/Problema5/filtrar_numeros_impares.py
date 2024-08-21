def problema5():
  numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  # Usando lambda para filtrar los números impares
  impares = list(filter(lambda x: x % 2 != 0, numeros))

  print(impares)


if __name__ == "__main__":
  problema5()
