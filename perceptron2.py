import numpy as np

# 3 entradas do neurônio
entradas = np.array([1, 7, 5])
# entradas = [-1, 7, 5]

# 3 pesos do neurôio
pesos = np.array([0.8, 0.1, 0])
# pesos = [0.8, 0.1, 0]

# função que somará¡ as multiplicaões das entradas com as saí­das
def soma(e, p):
    
    # dot product: produto escalar de dois vetores
    # mais eficiente do que fazer "manualmente"
    return e.dot(p)
    # manualmente:
    """
    s = 0
    for i in range(3):
        #print(e[i])
        #print(p[i])
        s += e[i] * p[i]
    return s
    """
        
s = soma(entradas, pesos)

# função degral
def stepFunction(soma):
    if soma >= 1:
        return 1
    return 0

r = stepFunction(s)