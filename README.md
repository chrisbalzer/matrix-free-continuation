## Matrix Pseudo-Arclength Continuation
Pseudo-arclength continuation (PAC) is a powerful tool for exploring solutions to non-linear problems without presupposing a path. Typcial solving methods that rely on iterative solvers, quasi-Newton, or Newton solvers are unusable near turning points. However, combined with PAC, some of these methods can find solution turning points (folds). This repository goes through a few examples demonstrating this observation.

### Toy Example
Detailed demonstration different algorithms of PAC for solving the root of the following equation. 

$ g(u,\lambda) = (u^2-1)(u^2 - 4) + \lambda u^2 e^{u/10} = 0$