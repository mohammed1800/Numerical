import sympy as sp

def compute_gradient_hessian():
    # Define symbolic variables
    x1, x2 = sp.symbols('x1 x2')

    # Define the function
    f = 100 * (x2 - x1**2)**2 + (1 - x1)**2

    # Compute the gradient
    gradient = [sp.diff(f, var) for var in (x1, x2)]

    # Compute the Hessian
    hessian = [[sp.diff(gradient[i], var) for var in (x1, x2)] for i in (0, 1)]

    return gradient, hessian

def main():
    gradient, hessian = compute_gradient_hessian()

    print("Gradient:")
    print(gradient)

    print("\nHessian:")
    print(hessian)

if __name__ == "__main__":
    main()
#the output:
#Gradient:
#[-400*x1*(-x1**2 + x2) + 2*x1 - 2, -200*x1**2 + 200*x2]

#Hessian:
#[[1200*x1**2 - 400*x2 + 2, -400*x1], [-400*x1, 200]]
