# 3 entradas do neur�nio
entradas = [-1, 7, 5]

# 3 pesos do neur�io
pesos = [0.8, 0.1, 0]

# fun��o que somar� as multiplica�es das entradas com as sa�das
def soma(e, p):
    s = 0
    for i in range(3):
        #print(e[i])
        #print(p[i])
        s += e[i] * p[i]
    return s
        
s = soma(entradas, pesos)

# fun��o degral
def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

r = stepFunction(s)