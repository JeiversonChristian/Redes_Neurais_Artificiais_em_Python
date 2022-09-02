# 3 entradas do neurônio
entradas = [-1, 7, 5]

# 3 pesos do neurôio
pesos = [0.8, 0.1, 0]

# função que somará¡ as multiplicaões das entradas com as saí­das
def soma(e, p):
    s = 0
    for i in range(3):
        #print(e[i])
        #print(p[i])
        s += e[i] * p[i]
    return s
        
s = soma(entradas, pesos)

# função degral
def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

r = stepFunction(s)