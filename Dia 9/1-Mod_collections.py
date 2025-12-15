from collections import Counter, defaultdict
numeros = [8, 6, 9, 5, 4, 5, 5, 8, 7, 4, 5, 4, 4]
print(Counter(numeros)) 

print(Counter("mississippi"))

frase = 'al pan pan y al vino vino'

print(Counter(frase.split()))

serie = Counter([1, 1, 2, 3, 4, 4, 4, 5, 5, 5, 5])
print(serie.most_common(1))
print(serie.most_common(3))
print(list(serie))
# Conta a frequência de cada número na lista
print('-----------------------------------')