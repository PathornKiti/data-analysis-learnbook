# Math notes: Module 3 (vectors and matrices)

## Vectors
A **vector** is an ordered list of numbers, e.g. a student $x = (10, 7)$ = (study hours, sleep hours).
Geometrically it's an arrow or a point. Two basic operations, done element by element:

* **Addition:** $(3,4)+(1,2)=(4,6)$
* **Scaling:** $2\cdot(3,4)=(6,8)$

## Length (norm) and distance
$$\lVert u\rVert=\sqrt{u_1^2+u_2^2+\dots+u_n^2}$$
This is Pythagoras in $n$ dimensions. The **distance** between $u$ and $v$ is $\lVert u-v\rVert$.
"Which customers are most similar?" often means "which vectors are closest?".

## Dot product
$$u\cdot v=\sum_{i=1}^{n}u_iv_i$$
Multiply matching entries, add them up. Interpretations:

* A **weighted sum**: the weights $(2,3)$ applied to $(10,7)$ give $2\cdot10+3\cdot7=41$.
* Related to the angle between vectors: $u\cdot v=\lVert u\rVert\lVert v\rVert\cos\theta$. It's 0 when the vectors are perpendicular.

A linear model $\hat{y}=b+w_1x_1+w_2x_2$ is just a dot product plus an intercept. You'll fit these in Module 9.

## Matrices
A **matrix** is a rectangular table of numbers with *rows × columns*. A dataset with 200 students and 3 measurements
is a $200\times3$ matrix $X$. If $w$ has 3 weights, then $Xw$ is a vector of 200 predictions, one dot product per row.
That's what `X @ w` computes.

Shapes must line up: $(m\times n)\,(n\times p)\to(m\times p)$. The inner numbers must match.

## Standardising: z-scores
$$z_i=\frac{x_i-\bar{x}}{s}$$
Subtract the mean (centre at 0), divide by the standard deviation (unit spread). It lets you compare things measured on
different scales, e.g. "is a 75 in Maths more impressive than an 82 in History?" depends on each class's mean and spread.

## Check your understanding
1. What is the length of $(6,8)$? (10)
2. What is $(1,2,3)\cdot(4,5,6)$? (4 + 10 + 18 = 32)
3. If $X$ is $5\times3$, what is the shape of $Xw$ when $w$ has 3 entries? ($5$ predictions)
