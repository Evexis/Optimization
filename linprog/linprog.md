REALIZOWANY PRZYKŁAD:

Minimize: f = -1*x[0] + 4*x[1]

Subject to: -3*x[0] + 1*x[1] <= 6
1*x[0] + 2*x[1] <= 4
x[1] >= -3



FUNKCJA LINPROG OGÓLNIE:

scipy.optimize.linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, method='simplex', 
      callback=None, options={'maxiter': 1000, 'disp': False, 'tol': 1e-12, 'bland': False})

c: Współczynniki liniowej funkcji celu, które mają być zminimalizowane
A_ub: Tablica dwuwymiarowa, która, gdy macierz pomnożymy przez x, podaje wartości więzów górnej nierówności w punkcie x
b_ub: Tablica jednowymiarowa wartości reprezentujących górną granicę każdego więzu nierówności (rzędu) w A_ub
A_eq: Tablica dwuwymiarowa, która, gdy macierz pomnożymy przez x, podaje wartości więzów równości w punkcie x
b_eq: Tablica jednowymiarowa wartości reprezentujących RHS każdego wiązania równości (rzędu) w A_eq
bounds: Granice dla każdej niezależnej zmiennej w rozwiązaniu. Forma NONE oznacza domyślne wartości graniczne, gdzie wszystkie 
      zmienne są nieujemne.
callback: Jeśli jest zapewniona funkcja callback, zostanie ona wywołana w każdej iteracji algorytmu simplex
