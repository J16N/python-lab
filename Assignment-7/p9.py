import numpy as np

N = int(input("Enter the number of equations: "))
vars = int(input("Enter the no. variables: "))
eqns = []
constMat = []

for i in range(N):
    print(f"\nEquation-{i + 1}")
    print()

    coeffs = [float(input(f"X{i} - ")) for i in range(vars)]
    eqns.append(coeffs)

    constMat.append(float(input(f"Constant{i} - ")))

a = np.array(eqns)
b = np.array(constMat)
print(f"Solution of system of linear equations = {np.linalg.solve(a, b)}")