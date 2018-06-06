scipy.optimize.approx_fprime(xk, f, epsilon, *args)

Głównym zastosowaniem approx_fprime jest optymalizacja funkcji skalarnych
w celu numerycznego określenia jakobianów funkcji.

Gradient funkcji jest określony:
      f(xk[i] + epsilon[i]) - f(xk[i])
f'[i] = ---------------------------------
                    epsilon[i]

Parametry:
xk - wektor współrzędnych, dla których będzie wyznaczony gradient f.

f - funkcja określajaca gradient (pochodne cząstkowe). Pobiera xk jako pierwszy argument. Zwraca wartość funkcji we współrzędnych xk.

Epsilon - dodawany do wartości współrzędnych xk w celu określenia gradientu funkcji.
Jeśli jest to skalar używa tej samej delty dla wszystkich pochodnych cząstkowych. Jeśli jest to tablica, powinna zawierać jedną wartość na każdy element xk.

*args - opcjonalny parametr, przekazujący argumenty do funkcji f

Return:
Pochodne cząstkowe funkcji f dla xk.


