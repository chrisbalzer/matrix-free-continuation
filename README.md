## Matrix-free Pseudo-Arclength Continuation
Pseudo-arclength continuation (PAC) is a powerful tool for exploring solutions to non-linear problems without presupposing a path. Typcial solving methods that rely on iterative solvers, quasi-Newton, or Newton solvers are unusable near turning points. However, combined with PAC, some of these methods can find solution turning points (folds). 

For large non-linear problems, matrix-free methods are attractive since Newton's method requires evaluation of the Jacobian. PAC is well-defined and guaranteed to work with Newton's method. Matrix-free methods do not have this guarenteed to work, but some of them work anyway! This repository goes through a few examples demonstrating this observation.

### Toy Example
Detailed demonstration different algorithms of PAC for solving the root of the following equation. 

$ g(u,\lambda) = (u^2-1)(u^2 - 4) + \lambda u^2 e^{u/10} = 0$