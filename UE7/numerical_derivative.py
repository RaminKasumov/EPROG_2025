def diff(f, h0, eps, x=0.0):
    h = h0
    phi_old = (f(x + h) - f(x)) / h

    while True:
        h /= 2
        phi_new = (f(x + h) - f(x)) / h

        if abs(phi_old - phi_new) <= eps * abs(phi_old):
            return phi_new

        phi_old = phi_new