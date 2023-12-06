import numpy as np
import matplotlib.pyplot as plt

# Format plot
plt.style.use('seaborn-v0_8-dark-palette')
plt.rcParams.update({
        "font.weight": "bold",  # bold fonts
        "lines.linewidth": 2,   # thick lines
        "lines.color": "k",     # black lines
        "savefig.dpi": 300,     # higher resolution output
        'text.usetex': True,
        "font.family": "serif",
        "font.serif": ['Computer Modern']
    })

# the function g(u,lambda)
def g(u,lam):
    return (u**2 - 1)*(u**2 - 4) + lam* u**2 * np.exp(u/10)

# the partial derivative of g(u,lambda) with respect to u
def gu(u,lam):
    return u*(lam*np.exp(u/10)*(u/10 + 2) + 4*u**2 - 10)

# a Newton step in u (only one variable so it's simple)
def newtonStep(ui,lam):
    return ui - g(ui,lam)/gu(ui,lam)

# solver that takes many Newton steps from a starting point u0
def newtonSolve(u0,lam):
    u = u0
    
    error = g(u,lam)
    maxIters = 1e3
    errorTol = 1e-12
    
    iteration = 0
    while np.abs(error) > errorTol:
        u = newtonStep(u,lam)
        error = g(u,lam)
        
        if iteration > maxIters:
            print('Exceeded maximum iterations')
            break
    return u


if __name__ == "__main__":
    # Calculate solution curve up to the turning point
    us = []
    lams = np.arange(0,0.869,0.001)
    for lam in lams:
        if lam == 0:
            u0 = 1.0
        else:
            u0 = u
        u = newtonSolve(u0,lam)
        us.append(u)
    
    # Save figure of solution
    f = plt.figure(figsize=(3, 2))
    plt.plot(lams,us)
    plt.xlabel('$\lambda$')
    plt.ylabel('$u$')
    plt.xlim([0,1])
    plt.ylim([0.5,2.5])
    f.savefig('figures/toyExampleNewton.png', bbox_inches='tight')
    
    