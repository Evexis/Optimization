def rosen(x):
    """
    Funkcja Rosenbrocka.
    Funkcja jest obliczana na podstawie::
        sum(100.0*(x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)
    Parametry
    ----------
    x : tablica
        Jednowymiarowa tablica punktów na których będzie liczona funkcja Rosenbrocka.
    Typ zwracany
    -------
    f : float
        Wartość funkcji Rosenbrocka.
    """
    x = asarray(x)
    r = numpy.sum(100.0 * (x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0,
                  axis=0)
    return r

def rosen_der(x):
    """
    Pochodna funkcji Rosenbrocka
    Parametry
    ----------
    x : tablica
        Jednowymiarowa tablica punktów na których będzie liczona pochodna funkcji Rosenbrocka.
    Typ zwracany
    -------
    rosen_der : (N,) tablica n-wymiarowa
        Gradient fukncji Rosenbrocka w punkcie 'x'
    """
    x = asarray(x)
    xm = x[1:-1]
    xm_m1 = x[:-2]
    xm_p1 = x[2:]
    der = numpy.zeros_like(x)
    der[1:-1] = (200 * (xm - xm_m1**2) -
                 400 * (xm_p1 - xm**2) * xm - 2 * (1 - xm))
    der[0] = -400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0])
    der[-1] = 200 * (x[-1] - x[-2]**2)
    return der


def rosen_hess(x):
    """
    Hesjan funkcji Rosenbrocka
    Parametry
    ----------
    x : tablica
        Jednowymiarowa tablica punktów na których będzie liczony hesjan funkcji Rosenbrocka.
    Typ zwracany
    -------
    rosen_hess : tablica n-wymiarowa
        Hesjan fukncji Rosenbrocka w punkcie 'x'
    """
    x = atleast_1d(x)
    H = numpy.diag(-400 * x[:-1], 1) - numpy.diag(400 * x[:-1], -1)
    diagonal = numpy.zeros(len(x), dtype=x.dtype)
    diagonal[0] = 1200 * x[0]**2 - 400 * x[1] + 2
    diagonal[-1] = 200
    diagonal[1:-1] = 202 + 1200 * x[1:-1]**2 - 400 * x[2:]
    H = H + numpy.diag(diagonal)
    return H


def rosen_hess_prod(x, p):
    """
    Mnożenie hesjana fukncji Rosenbrocka z wektorem.
    Parametry
    ----------
    x : tablica
        Jednowymiarowa tablica punktów na których będzie liczony hesjan funkcji Rosenbrocka.
    p : tablica
        Mnożnik hesjana funkcji Rosenbrocka
    Typ zwracany
    -------
    rosen_hess_prod : tablica n-wymiarowa
        Przemnożony przez 'p' hesjan fukncji Rosenbrocka w punkcie 'x'.
    """
    x = atleast_1d(x)
    Hp = numpy.zeros(len(x), dtype=x.dtype)
    Hp[0] = (1200 * x[0]**2 - 400 * x[1] + 2) * p[0] - 400 * x[0] * p[1]
    Hp[1:-1] = (-400 * x[:-2] * p[:-2] +
                (202 + 1200 * x[1:-1]**2 - 400 * x[2:]) * p[1:-1] -
                400 * x[1:-1] * p[2:])
    Hp[-1] = -400 * x[-2] * p[-2] + 200*p[-1]
    return Hp
