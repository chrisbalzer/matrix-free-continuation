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

# the solution give lambda given a value of u
def lam(u):
    return -(u**2 - 1)*(u**2 - 4)/(u**2 * np.exp(u/10))

if __name__ == "__main__":
    # Calculate solution curve up to the turning point
    us = np.arange(1,2.001,0.001)
    lams = []
    for u in us:
        lams.append(lam(u))
    
    # Save figure of solution
    f = plt.figure(figsize=(3, 2))
    plt.plot(lams,us)
    plt.xlabel('$\lambda$')
    plt.ylabel('$u$')
    plt.xlim([0,1])
    plt.ylim([0.5,2.5])
    f.savefig('figures/toyExampleFull.png', bbox_inches='tight')