import numpy as np


def f(x):
    return np.exp(np.sin(np.log(1 + x**2))) + (x-1)**2

def gradient(f, x, deltax):
    # FYLL INN
    teller = f(x + deltax) - f(x - deltax)
    nevner = 2* deltax
    svar = teller/nevner
    return svar

x = 4.0
deltax = 0.0000001
stegLengde = 0.01
toleranse = 0.01
feil = gradient(f, x, deltax)
maxAntallSteg = 1000
antallSteg = 1

while abs(feil) > toleranse and maxAntallSteg > antallSteg:
    nyGradient = gradient(f, x, deltax)
    x = x - stegLengde * nyGradient
    feil = nyGradient
    antallSteg = antallSteg + 1