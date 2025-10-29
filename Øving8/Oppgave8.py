import numpy as np

LARGE = 10
def funk(x):
    # Rosenbrock (med parameter)
    return LARGE*(x[1]-x[0]**2)**2 + (1-x[0])**2

def gradfunk(x):
    # Rosenbrock gradient (med parameter)
    return np.array([-4*LARGE*((x[1]-x[0]**2))*x[0]-2*(1-x[0]), 2*LARGE*(x[1]-x[0]**2)])

x0 =  np.array([-1,1.5])
funk0 = funk(x0)
grad0 = gradfunk(x0)

def line_search_1(f, x, d, f0, N_fin = 100):
    # linjesoek via fin dikretisering (brute force)
    tt = np.linspace(0, 1, N_fin)
    fmin = f0
    use_indeks = 0  
    for i in range(1, N_fin):
        ftest = f(x + tt[i]*d) # funksjonsverdi som testes
        if ftest < fmin:
            use_indeks = i
            fmin = ftest
    if use_indeks == 0:
        # ingen bedre verdi funnet
        return None
    else:
        # vanligvis gir en saann funksjon tt[use_indeks], 
        # men det blir enklere for denne oppgaven
        return x+tt[use_indeks]*d


def line_search_2(f, x, d, f0, grad0, n_max = 10, rho=0.6, c=0.8):
    n = 0
    alpha = 1
    while n < n_max:
        # 
        fnew = f(x + alpha*d) # funksjonsverdi som testes
        flin =f0 + c*alpha*np.dot(grad0,d) # funksjonsverdi av den lineære funksjonen den sammenlignes med
                   # Du kan (burde) bruke np.dot og/eller np.inner her.
        if fnew <= flin:
            # Armijo betingelse tilfredsstilt
            return x+alpha*d
        else:
            n += 1
            alpha = alpha*rho
    if n == n_max:
        return None

resultat_linjesoek1 = line_search_1(funk, x0, funk0, -grad0, funk0, N_fin=60)
resultat_linjesoek2 = line_search_2(funk, x0, -grad0, funk0, grad0, n_max=10, rho=0.4, c = 0.8)