#Minimize

### Problem
Postawionym problemem było znalezienie wartości zmiennych *x1*, *x2*, *x3* i *x4* dla których poniższe równanie przyjmuje minimum 

```math
\min{ x_{1}x_{4}(x_{1}-x_{2}++x_{3})-x_{2}}
```
Przy założeniach:

```math
    x_{1}x_{2}x_{3}x_{4} \geq 25 
```
```math 
    x_{1}^{2} + x_{2}^{2} + x_{3}^{2} * x_{4}^{2} = 40
```
```math 
    x_{1}x_{2}x_{3}x_{4}-x_{1} \geq 30 
``` 

```math 
     x_{1}x_{2} \geq x_{3}x_{4}
```

oraz zakładjąc że zmienne należą do liczb rzczywistych ograniczonych przedziałem _<-10, 10>_

```math 
    -10 \leq x_{1},x_{2},x_{3},x_{4} \leq 10
```

###Rozwiązanie
Korzystając z języka *python* oraz modułu *scipy.ptimization* zawierającego między innymi funkcję ***minimize()*** stworzono skrypt *minimize.py* rozwiązujący wyżej opisany problem.
Funkcja ***minimize()*** używa jednej z predefiniowanych dla siebie metod rozwiązywania problemów optymalizacji. Wyboru dokonuje się z poniższej listy.


* Nelder-Mead
* Powell
* CG
* BFGS
* Newton-CG
* L-BFGS-B
* TNC
* COBYLA
* SLSQP
* trust-const
* dogleg
* trust-ncg
* trust-exact
* trust-krylov 

W tej implementacji używa się metody ***SLSQP***.
Funkcja *minimize()* potrzebuje również wartości inizjalizujących proces znajdywania minimum, żałozone zostało, że:
```math
[x_{1},x_{2},x_{3},x_{4}] = [-7,2,5,1]
```

###Wyniki
Rezultat optymalizacja są następujące:
![alt](/minimize/pictures/brief.PNG)

Szczegółowy wynik zwaracny przez funkcję *minimize()* wygląda natomiast tak:
![alt](/minimize/pictures/full.PNG)