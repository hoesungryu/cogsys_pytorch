# lec_04 asnwer
# Q1. 
a = np.array([[9, 5, 0],
              [9, 5, 0],
              [5, 4, 9]])
b = np.array([[5, 10, 5],
              [4, 4, 3],
              [6, 10, 4]])
c = np.array([10, 6, 9])



# sol1. 
v = a @ b @ c

# sol2. 
v = np.dot(np.dot(a, b), c)


# Q2. 
E = 80e10
L = 0.25

K = np.array([[0.00576, -0.00576, 0, 0],
              [-0.00576, 0.0095, -0.002687, 0],
              [0, -0.002687, 0.0075, -0.000733],
              [0, 0, -0.000733, 0.000733]])
# either works:
f = np.array([10000. / 6, 10000. / 3, 10000. / 3, 10000. / 6])
f = np.array([[10000. / 6],
              [10000. / 3],
              [10000. / 3],
              [10000. / 6]])
u = np.linalg.solve(E / L * K, f)
print(u)



# Q3.
x = np.array([0.0, 0.7, 1.7, 2.1])
y = np.array([1.1, 2.99, 5.69, 6.77])
A = np.vstack([x, np.ones(len(x))]).T
# or
A = np.array([x, np.ones(len(x))]).T
c, residuals, rank, sing = np.linalg.lstsq(A, y)
print(c)
print(residuals)
print(rank)
