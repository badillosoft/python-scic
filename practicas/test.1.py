import nltk
from nltk import FreqDist

raw_text = """
Hola mundo mundial; este es un texto
muy largo :D jeje soy Batman o Bruno Diaz.
Quien eres tu?
"""

tokens = nltk.word_tokenize(raw_text)

print(tokens)

text = nltk.Text(tokens)

print(text[:2])

fdist = FreqDist(text)

for k in fdist:
    print (k, fdist[k])

fdist.plot()