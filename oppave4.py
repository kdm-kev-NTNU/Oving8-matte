import numpy as np

def f(x):
    return np.sin(1.5 * x) + 0.1 * x**2 - 1.0

def gradient(x):
    return 1.5 * np.cos(1.5 * x) + 0.2 * x

# argumentet x0 er startverdien
def gradientmetode(x0):
    maxAntallSteg = 1000 # Maks antall steg som algoritmen vil utføre
    antallSteg = 1       # Antall steg vi har utført så langt
    tol = 0.01           # Toleranse for testen grad == 0
    stegLengde = 0.05
    x = x0               # startposisjon

    ferdig = False

    while not ferdig: 
        nyGradient = gradient(x)
        feil = abs(nyGradient)
        x = x - stegLengde * nyGradient  #xk+1 = xk -a*Pk
        antallSteg = antallSteg + 1
        print(f"Steg: {antallSteg}, x = {x}")
    
        if feil < tol or maxAntallSteg <= antallSteg: ferdig = True
    
    if maxAntallSteg <= antallSteg:
        print("Algoritmen ble avsluttet fordi den kjørte for lenge")

    return x

x0 = -1
x = gradientmetode(x0)
fun = f(x)
print(f"Med x0 = {x0} får vi svaret x = {x}, med funksjonsverdi f(x) = {fun}")