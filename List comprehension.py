x = [1,2,3,4,5]
y = [i**2 for i in x] #eleva ao quadrado os termos da lista x
print(y)
z = [i**2 for i in x if i%2==1] #eleva ao quadrado os termos ímpares de x
print(z)