palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

# Usando lambda para filtrar palabras con más de 5 letras
filtradas = list(filter(lambda palabra: len(palabra) > 5, palabras))

print(filtradas)
