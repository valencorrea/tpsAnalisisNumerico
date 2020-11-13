import numpy as np

def raiz(f, x0, tolerancia, iteraciones):
    xn = x0
    deltax = tolerancia + 1
    i = 0
    raices = [xn]
    cotas = ['-']

    while (deltax > tolerancia) and (i < iteraciones):
        i+=1
        temp = xn
        xn = f(temp)
        deltax = np.abs(f(xn) - f(temp))
        raices.append(xn)
        cotas.append(deltax)

    return raices, cotas