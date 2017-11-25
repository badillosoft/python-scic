import nltk.book as books

text = books.text2

print("-" * 10)

# El contexto de una palabra
#text1.concordance("MONSTROUS")

# Palabras en contextos simalares
#text1.similar("monstrous")

# Ver los contextos similares entre las palabras
#text.common_contexts(["monstrous", "very"])

# Graficar la dispersión de las palabras a lo largo del texto
#text.dispersion_plot(["monstrous", "very", "glad", "red"])

n = len(text)

print("Palabras en el texto: {}".format(n))

primary_words = sorted(set(text))

print(primary_words[-20:])

m = len(primary_words)

print("Palabras distintas en el texto: {}".format(m))

d = n / m

print("Diversidad lexica: {}".format(d))

# Frecuencia de palabras

from nltk import FreqDist

freq = FreqDist(text)

print("Frecuencia de <monstrous>: {}".format(freq["monstrous"]))
print("Frecuencia de <very>: {}".format(freq["very"]))

freq.plot(50, cumulative=True)