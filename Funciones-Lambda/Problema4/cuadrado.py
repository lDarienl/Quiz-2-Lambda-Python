def problema4():
  numeros = [2, 4, 6, 8, 10]
  
  # Usando lambda para elevar al cuadrado cada número
  cuadrados = list(map(lambda x: x**2, numeros))
  
  print(cuadrados)

if __name__ == "__main__":
  problema4()