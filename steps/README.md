### step 24
```bash
python step24.py
```
Sphere 함수
```math
z = x^2 + y^2
```
![](sphere.png)

matyas 함수
```math
z = 0.26(x^2 + y^2) - 0.48xy
```
![](matyas.png)

Goldstein-Price 함수
```math
f(x,y) = [1 + (x + y + 1)^2(19 - 14x + 3x^2 - 14y + 6xy + 3y^2)]  
         [30 + (2x - 3y)^2(18 - 32x + 12x^2 + 48y - 36xy + 27y^2)]
```
![](goldstein.png)

### step 27
```bash
python step27.py
```
sin 클래스  
테일러 급수 이론
```math
sin(x) = \frac{x}{1!} - \frac{x^3}{3!} + \frac{x^5}{5!} - ... = \sum^{\infty}_{i=0}(-1)^i\frac{x^{2i+1}}{(2i+1)!}
```
![](taylor_sin.png)

### step 28
```bash
python step28.py
```
함수 최적화
rosenbrock의 미분
```math
y = 100(x1 - x0^2)^2 + (1 - x0)^2
```
경사하강법 구현

### step 29
```bash
python step29.py
```
```math
y = x^4 - 2x^2
```

### step 30~32
고차 미분
순전파 계산 시 만들어진 계산 그래프를 역전파 계산에도 만들어서 고차 미분 자동화

### step 34
```bash
python step34.py
```

### step 35
```bash
python step35.py
```
tanh 클래스
```math
y = tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}
```

### step 36
```bash
python step36.py
```
double backprop
```math
y = x^2
```
```math
z = (\frac{\partial}{\partial x}y)^3 + y
```
```math
\frac{\partial}{\partial x}z = 24x^2 + 2x
```

### step 37
```bash
python step37.py
```

### step 38
```bash
python step38.py
```

### step 39
```bash
python step39.py
```

### step 40
```bash
python step40.py
```
sum
```math
gx1 = \sum gy
```
sub
```math
gx1 = \sum gy
```
mul
```math
gx1 = \sum gy\bullet x0
```
div
```math
gx1 = \sum -gy \frac{x0}{x1^2}
```

### step 41
```bash
python step41.py
```
```math
\frac{\partial L}{\partial x} = \sum \frac{\partial L}{\partial y} \frac{\partial y}{\partial x} = \sum \frac{\partial L}{\partial y} W^T
```
```math
\frac{\partial L}{\partial W} = x^T \frac{\partial L}{\partial y}
```

### step 42
```bash
python step42.py
```

### step 43
```bash
python step43.py
```