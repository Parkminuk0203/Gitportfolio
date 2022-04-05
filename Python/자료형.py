# 문자열(String, str) 자료형
a = "Hello"
b = 'world'
print(type(a)) # <class 'str'>
print(type(b)) # <class 'str'>

#부울(Boolean, bool) 자료형
a = True
b = False
print(type(a)) # <class 'bool'>
print(type(b)) # <class 'bool'>

a = (100 < 100)
print(a) # False
b = (300 == 300)
print(b) # True

#None 자료형
a = None
print(a) # None
print(type(a)) # <class 'NoneType'>

x = 10
y = 20
print(x + y) # 30

x = 'Hello'
y = 'World'
print(x + y) # Helloworld

# 반지름이 5.0인 원의 면적을 계산하는 프로그램을 작성하시오.
radius = 5.0
area = 3.141592 * radius * radius
print('원의 면적은', area) # 원의 면적은 78.5398

area = 3.141592 * radius**2
print('원의 면적은', area) # 원의 면적은 78.5398

# 체중(kg)과 키(m)를 변수에 넣어서 신체질량지수 BMI를 계산하여 출력하시오.

h = float(input("당신의 키(m)를 입력하시오: "))
w = float(input("당신의 몸무게(kg)를 입력하시오: "))

bmi = w / h**2 # **2는 2제곱 의미
print('BMI는', bmi)

# 부울 값 이해하기
b1 = True
b2 = False

print(b1) # True
print(b2) # False
print(3<4) # True
print(3>4) # False