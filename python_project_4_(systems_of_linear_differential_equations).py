# -*- coding: utf-8 -*-
"""MAT 220 Python Project 4 (Systems of Linear Differential Equations).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bGtxUrsHk-tGjei-q_7Mgn3SCa07GARV

# Python Project 4: Systems of Linear Differential Equations

Reference pages 380-381 (Section 7.4) (Subsection "Systems of Linear Differential Equations") of textbook

One application of eigenvalues/eigenvectors and diagonal matrices is the ability to solve systems of linear differential equations.

## Example
---

Consider the system of linear differential equations:

$y_1'=6y_1+y_2$

$y_2'=4y_1+3y_2$

We will use Python to find the eigenvalues and eigenvectors of the coefficient matrix. First, import the relevant libraries (sympy, numpy, matplotlib) and initialize variables. This has been our standard initialization
"""

# Initialization; Only need to run once.
from sympy import *
init_printing()
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

import matplotlib.pyplot as plt
import numpy as np
from sympy.plotting.plot import MatplotlibBackend, Plot

"""Enter the coefficient matrix:"""

A = Matrix([
    [6,1],
    [4,3]
])
pprint(A)

"""Let Python (via Sympy) find the eigenvectors and eigenvalues."""

A.eigenvects()

"""From this, we can see that the eigenvalue $\lambda_1=2$ has a multiplicity of 1 and a corresponding eigenvector of $v_1=\begin{bmatrix}-\frac{1}{4} \\ 1 \end{bmatrix}$ and the eigenvalue $\lambda_2=7$ has a multiplicity of 1 and a corresponding eigenvector of $v_2= \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.

---

*Note:*  We could also write $v_1=\begin{bmatrix}-1 \\ 4 \end{bmatrix}$ so that there are no fractions.

---

We now diagonalize $A$:
"""

P = Matrix([
    [-1,1],
    [4,1]
])
D = (P**-1)*A*P
pprint(D)

"""We see that $D$ is a diagonal matrix with the eigenvalues of $A$ on its diagonal.

We now need to solve the system:

$\begin{bmatrix}w_1' \\ w_2' \end{bmatrix} = \begin{bmatrix}2 & 0 \\ 0 & 7 \end{bmatrix} \begin{bmatrix}w_1 \\ w_2 \end{bmatrix}$

or $w'=D\cdot w$
"""

w1, w2 = symbols('w1 w2') # Initialize as sympy variables
W = Matrix([
    [w1],
    [w2]
])
D*W

"""This means that:

$w_1'=2w_1$

$w_2'=7w_2$

The system has been "un-tangled"! Solving these two equations using a general exponential and $t$ as our variable, we get the solution of the system is:

$w_1=C_1 e^{2t}$

$w_2 = C_2 e^{7t}$

Finally, we use the change of variables $y=P\cdot w$ to get:
"""

P*W

"""This gives us:

$\begin{bmatrix}y_1 \\ y_2 \end{bmatrix} = \begin{bmatrix}-w_1+w_2 \\ 4w_1+w_2 \end{bmatrix}$

So:

$y_1=-C_1 e^{2t}+C_2 e^{7t}$

$y_2=4C_1 e^{2t}+C_2 e^{7t}$

## Directions

+ **You must use methods from our class, as shown above**. Do not use new code methods or write your own. I am checking that you are using the built-in features, including the matrices.
+ Do not use other AI programs or create new functions that are not given.  Again, do not use new code methods or write your own.
+ Make sure you run each code cell with appropriate output visible. You must include all of the matrices in the appropriate place in your document.

For each problem below, solve the system of linear differential equations. Assume that each is a function of $t$. Be sure to label your answers properly.

## Problem 1

$y_1'=y_1-4y_2$

$y_2'=2 y_2$
"""

# Inital Matrix
A = Matrix([
    [1,-4],
    [0,2]
])
pprint(A)

# Find EigenVectors and Values
A.eigenvects()

# Diagonalize
P = Matrix([
    [1,-4],
    [0,1]
])
D = (P**-1)*A*P
pprint(D)

# Solve the System
w1, w2 = symbols('w1 w2') # Initialize as sympy variables
W = Matrix([
    [w1],
    [w2]
])
D*W

# Use the change of variables
P*W

"""## Problem 2

$y_1'=y_1+2y_2$

$y_2'=2y_1+y_2$
"""

# Inital Matrix
A = Matrix([
    [1,2],
    [2,1]
])
pprint(A)

# Find EigenVectors and Values
A.eigenvects()

# Diagonalize
P = Matrix([
    [1,1],
    [1,-1]
])
D = (P**-1)*A*P
pprint(D)

# Solve the System
w1, w2 = symbols('w1 w2') # Initialize as sympy variables
W = Matrix([
    [w1],
    [w2]
])
D*W

# Use the change of variables
P*W

"""## Problem 3

$y_1'=y_1-2y_2+y_3$

$y_2'=2y_2+4y_3$

$y_3'=3y_3$
"""

# Inital Matrix
A = Matrix([
    [1, -2, 1],
    [0, 2, 4],
    [0, 0, 3]
])
pprint(A)

# Find EigenVectors and Values
A.eigenvects()

# Diagonalize
P = Matrix([
    [1, -2, -7/2],
    [0, 1,  4],
    [0, 0,  1]
])
D = (P**-1)*A*P
pprint(D)

# Solve the System
w1, w2, w3 = symbols('w1 w2 w3') # Initialize as sympy variables
W = Matrix([
    [w1],
    [w2],
    [w3]
])
D*W

# Use the change of variables
P*W

"""So, y1 = C1(e^t) - 2C2(e^2t) - 7/2C3(e^3t), y2 = C2(e^2t) + 4C3(e^3t), y3 = C3(e^3t)"""