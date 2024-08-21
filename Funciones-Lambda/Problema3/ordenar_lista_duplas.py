def problema3():
  puntos = [(1, 2), (2, 3), (0, 1), (3, 3)]

  # Usando lambda para ordenar por la distancia al origen (0, 0)
  puntos_ordenados = sorted(puntos,
                            key=lambda punto: punto[0]**2 + punto[1]**2)

  print(puntos_ordenados)


if __name__ == "__main__":
  problema3()
