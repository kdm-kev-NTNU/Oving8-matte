import numpy as np

def compute_loss_grad_hess(x, c, w, mu):
    # beregn maalfunksjonen, dens gradient og hessematrisa,
    # IKKE FORANDRE DENNE KODEN
    M, N = len(x), len(c)
    l, g, H = 0.0, np.zeros(M), np.zeros((M,M))
    tw = np.sum(w)
    for j in range(M):
        for i in range(N):
            d = c[i] - x[j]
            l += w[i] * d**2
            g[j] -= 2 * w[i] * d
        H[j,j] += 2 * tw

    if mu > 0.0:
        l+= -mu * ( np.log(x[1] - x[0]) + np.log(x[2] - x[1]) )
        g[0] +=  mu / (x[1] - x[0])
        g[1] += -mu / (x[1] - x[0]) + mu / (x[2] - x[1])
        g[2] += -mu / (x[2] - x[1])
        H[0,0] +=  mu / (x[1] - x[0])**2
        H[0,1] +=  -mu / (x[1] - x[0])**2
        H[1,0] +=  H[0,1]
        H[1,1] +=  mu / (x[1] - x[0])**2 + mu / (x[2] - x[1])**2
        H[1,2] +=  -mu / (x[2] - x[1])**2
        H[2,1] +=  H[1,2]
        H[2,2] +=  mu / (x[2] - x[1])**2
    return l, g , H
    

c = np.array([0.0, 0.2, 0.5, 0.7, 1.0]) # romplassering
w = np.array([0.1, 0.2, 0.2, 0.1, 0.4]) # vekting av rom
mu = 0.01 

x = np.array([0.1, 0.4, 0.8])  # Initialgjett, merk x_1 < x_2 < x_3

all_x, all_d = [x], []
for i in range(10):
    # Vi avslutter her etter maksimalt 10 iterasjoner, 
    loss, grad, hess = compute_loss_grad_hess(x,c,w,mu)
    if np.linalg.norm(grad) < 1e-8:
        # Bryt hvis gradienten er tilnærmet null
        break
    
    #===============
    #Fyll inn beregningen av steget
    d = -np.linalg.inv(hess)@grad
    #===============
    
    x = x + d
    
    all_x.append(x)
    all_d.append(d)

