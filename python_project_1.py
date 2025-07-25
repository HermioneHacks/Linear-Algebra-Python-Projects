# -*- coding: utf-8 -*-
"""MAT 220 Python Project 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OMuWhhkmiKDYc57Bjzz52GDFYRaNaIQU

# Python Project 1: Polynomial Curve Fitting

*Reference page 25 in Section 1.3 of the Larson textbook.*

Given $n + 1$ data points with distinct x-coordinates, $(x_1, y_1), (x_2, y_2), … , (x_n, y_n), (x_{𝑛+1}, y_{n+1})$,
there will be a unique polynomial of degree at most $n$ whose graph passes through the points.

The polynomial will take the form of:
$P_n(x) = a_n x_n + a_{𝑛−1}x_{𝑛−1} + ⋯ + a_1x + a_0$

## **Example**

Given the following $n + 1$ data points, find the polynomial with degree at most $n$ that fits these data points.

(1,3), (2,5), and (3,3)

**Solution:**

There are three data points, so the polynomial degree will be 2:

$P_2(x) = a_2x^2 + a_1x + a_0$

System:

(1,3): $P_2(1) = a_2(1)^2 + a_1(1) + a_0 = 3 ⟹ 1a_2 + 1a_1 + a_0 = 3$

(2,5): $P_2(2) = a_2(2)^2 + a1(2) + a_0 = 5 ⟹ 4a_2 + 2a_1 + a_0 = 5$

(3,3): $P_2(3) = a_2(3)^2 + a1(3) + a_0 = 3 ⟹ 9a_2 + 3a_1 + a_0 = 3$

Matrix Representation:
$$ \begin{bmatrix}
1 & 1 & 1 &| 3 \\
4 & 2 & 1 &| 5 \\
9 & 3 & 1 &| 3
\end{bmatrix}  $$

Solve this system using Python:
"""

from sympy import *
init_printing()
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
M=Matrix([
    [1,1,1,3],
    [4,2,1,5],
    [9,3,1,3]
])
R=M.rref()[0]
R

"""Now that we have the polynomial, let’s use Python and matplotlib to display the graph of the polynomial."""

import matplotlib.pyplot as plt
plot(-2*x**2+8*x-3, line_color='red')

"""## Directions for Problems 1–4

Now you try the following:

+ You must use methods from class.
+  Do not use other AI programs or create new functions that are not given.
+ Download the project as a PDF to upload to the assignment dropbox.
+ Make sure that all code and matrix/graphics outputs are visible in your PDF.

Steps for each problem (given the $n + 1$ data points):
+ Use the data points to create a matrix on paper.
+ Using Jupyter and the matrix you created on paper, create matrix M as shown above.
+ Print matrix M in Jupyter, then copy the matrix into your document.
+ Use the RREF feature of Sympy to reduce your matrix M.
+ Find the polynomial with degree at most n that fits these data points.
+ Then code in Python to display a graph of the polynomials.

### Problem 1

Points: $(-1, -9), (-2,8), (3, -57), (2, -12)$
"""

from sympy import *
init_printing()

x, y, z, t, h = symbols('x y z t h')
k, m, n, o = symbols('k m n o', integer=True)
f, g, k, l = symbols('f g k l', cls=Function)

M = Matrix([
    [-1,  1, -1, 1,  -9],
    [-8,  4, -2, 1,   8],
    [27,  9,  3, 1, -57],
    [ 8,  4,  2, 1, -12],
])

R = M.rref()[0]
display(R)

#plot functions!
import matplotlib.pyplot as plt
# define symbol and polynomial
P = -3*x**3 + x**2 + 7*x - 6

# plot with Sympy’s plot()
plot(P, line_color='red')

"""### Problem 2

Points: $(1,1), (-3,365), (-2,112), (3,47), (4,232)$
"""

from sympy import *
init_printing()

x, y, z, t, h, i = symbols('x y z t h i')
k, m, n, o, p = symbols('k m n o p', integer=True)
f, g, k, l, r = symbols('f g k l r', cls=Function)

M = Matrix([
    [  1,   1,  1,  1, 1,   1],
    [ 81, -27,  9, -3, 1, 365],
    [ 16,  -8,  4, -2, 1, 112],
    [ 81,  27,  9,  3, 1,  47],
    [256,  64, 16,  4, 1, 232],
])

R = M.rref()[0]
display(R)

#plot functions!
import matplotlib.pyplot as plt
# define symbol and polynomial
P = 2*x**4 + -5*x**3 + 4*x**2 + -8*x + 8

# plot with Sympy’s plot()
plot(P, line_color='red')

"""### Problem 3

Points: $(1, -1), (-2,221), (2, -27), (-3,1343), (3, -349), (-1,3)$
"""

from sympy import *
init_printing()

x, y, z, t, h, i, j = symbols('x y z t h i j')
k, m, n, o, p, q = symbols('k m n o p q', integer=True)
f, g, k, l, r, s = symbols('f g k l r s', cls=Function)

M = Matrix([
    [   1,    1,   1,  1,   1,  1,   -1],
    [ -32,   16,  -8,  4,  -2,  1,  221],
    [  32,   16,   8,  4,   2,  1,  -27],
    [-243,   81, -27,  9,  -3,  1, 1343],
    [ 243,   81,  27,  9,   3,  1, -349],
    [  -1,    1,  -1,  1,  -1,  1,    3],
])

R = M.rref()[0]
display(R)

#plot functions!
import matplotlib.pyplot as plt
# define symbol and polynomial
P = -3*x**5 + 6*x**4 + -5*x**3 + 2*x**2 + 6*x + -7

# plot with Sympy’s plot()
plot(P, line_color='red')

"""### Problem 4

The following table gives the global smartphone sales to end users in millions from 2007 to 2012. Use $x$ to be the number of years after 2007.

| Year              | 2007   | 2007   | 2009   | 2010   | 2011 | 2012   |
|-------------------|--------|--------|--------|--------|------|--------|
| Sales in millions | 122.32 | 139.29 | 172.38 | 296.65 | 472  | 680.11 |

(a) Follow all of the above directions for question 4:
"""

from sympy import *
init_printing()

x, y, z, t, h, i, j = symbols('x y z t h i j')
k, m, n, o, p, q = symbols('k m n o p q', integer=True)
f, g, k, l, r, s = symbols('f g k l r s', cls=Function)

M = Matrix([
    # Use x to be the number of years after 2007
    [    0,    0,   0,  0, 0, 1, 122.32],
    [    1,    1,   1,  1, 1, 1, 139.29],
    [   32,   16,   8,  4, 2, 1, 172.38],
    [  243,   81,  27,  9, 3, 1, 296.65],
    [ 1024,  256,  64, 16, 4, 1, 472   ],
    [ 3125,  625, 125, 25, 5, 1, 680.11],
])

R = M.rref()[0]
display(R)

#plot functions!
import matplotlib.pyplot as plt
# define symbol and polynomial
P = 1.14116666666656*x**5 + -16.2099999999986*x**4 + 81.240833333327*x**3 + -139.309999999989*x**2 + 90.1079999999943*x + 122.32

# plot with Sympy’s plot()
plot(P, (x, 0, 5), line_color='red')

"""(b) Lastly compare your polynomial to the bar graph at:

https://www.statista.com/statistics/263437/global-smartphone-sales-to-end-users-since-2007/

Is the polynomial a good fit for all of the data presented in the bar chart? Why or why not?

(Edit this text cell to document your answer to part (b) above.)
"""

# For up to 2012, yes, it's good, but since there are no points till 2023,
# it would not portray the full bar chart
# showing it may not be fully similar. In conclusion, looking at all of
# the data on the bar chart, this polynomial is not a good fit due to the
# points stopping at an x of 2012.