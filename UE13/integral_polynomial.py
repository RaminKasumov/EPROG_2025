import sympy as sp

x, a, b = sp.symbols('x a b')

c0, c1, c2, c3 = sp.symbols('c0 c1 c2 c3')
p = c0 + c1*x + c2*x**2 + c3*x**3

basis = [1, x, x**2, x**3]

equations = []
for q in basis:
    equations.append(
        sp.integrate(p*q, (x, a, b)) - q.subs(x, b)
    )

solution = sp.solve(equations, [c0, c1, c2, c3])

p_solution = sp.simplify(p.subs(solution))

print(f"The unique polynomial p(x) is: {p_solution}")