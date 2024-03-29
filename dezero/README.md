```bash
python main.py
```

### step 03
합성 함수  
```math
y = (e^{x^2})^2
```
### step 04
수치 미분 : 미세한 차이를 이용하여 함수의 변화량을 구하는 방법  
계산 비용과 정확도면에서 문제가 있음

### step 05~06
역전파

### step 07
역전파 자동화  
linked list 구조 이용

### step 09


### step 11
인수와 반환값을 리스트로 변경  
가변 길이 인수 사용
```math
y = x_0 + x_1
```

### step 13
가변 길이 인수 역전파
```math
y = x^2 + y^2
```

### step 14
같은 변수 반복 사용
```math
y = x + x + x = 3x
```
미분값 재설정
```math
y = x + x  
y = x + x + x
```

### step 15~16
복잡한 계산 그래프  
다양한 위상의 계산 그래프에 대응  
세대 수가 큰 쪽부터 처리  
```math
y = (x^2)^2 + (x^2)^2
```
```mermaid
graph LR;
    A(x)-->B[A];
    B-->C(a);
    C-->D[B];
    C-->E[C];
    D-->F(b);
    E-->G(c);
    F-->H[D];
    G-->H;
    H-->I(y);
```

### step 17
메모리 관리와 순환 참조  
파이썬의 메모리 관리는 `참조 카운트`와 `가비지 컬렉션` 두 가지 방식으로 진행  
순환 참조를 방지하기 위해 weakref 모듈 사용  
다른 객체를 참조하되 참조 카운트는 증가시키지 않는 방식  

### step 18
`retain_grad`로 말단 변수 외에는 미분값 유지하지 않음  
`enable_backprop`로 예측 시 순전파 연산만 사용


### step 19
변수 사용성 개선  

### step 20
Mul 클래스  
float, int와 함께 사용
Neg, Sub, Div, Pow 클래스