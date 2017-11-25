from nltk.book import text1
from nltk import FreqDist

freq = FreqDist(text1)

# Buscar todas las palabras de logitud 5
# con frecuencia mayor a 20

words = [ word for word in set(text1) if len(word) == 5 and freq[word] >= 400 ]

print(words)