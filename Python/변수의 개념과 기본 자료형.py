# 변수 : 값을 저장하는 공간
# 형식 : 변수이름 = 값
# 변수를 선언한다
# 변수는 선언을 해야 사용 할 수 있음
# 데이터를 저장할 수 있는 공간을 할당하고 특별한 이름(변수명)을 부여하는 과정을 선언한다고 함
# 데이터를 저장하는 공간 : 변수
# 변수는  컴퓨터의 메모리 공간의 특정 위치에 이름을 붙여서 정수, 실수, 문자열 등의 데이터를 저장하는 것
# 변수의 값은 수시로 바뀔 수 있다

# 파이썬에서는 변수 여러 개를 한 번에 만들 수도 있다.
x, y, z = 10, 20, 30
print(x, y, z)
#10 20 30

# 변수 여러 개를 만들 때 값이 모두 같아도 된다면 
x = y = z = 10
print(x, y, z)
#10 10 10

# 두 변수의 값을 바꾸려면 다음과 같이 변수를 할당할 때 서로 자리를 바꿔주면 됨
x , y = 10, 20
x, y = y, x
print(x) 
#20
print(y)
#10

# 변수에는 숫자 뿐만 아니라 문자열도 넣을 수 있다.
x = "Hello World!"
print(x)
#Hello World!

# 프로그래밍 분야에서는 텍스트(Text, 글자) 데이터를 문자열(String) 이라고 함
# 파이썬에서의 문자열은 큰따옴표("...")나 작은따옴표('...')를 이용해서 만든다.
s1 = "Hello" 
s2 = "World"
print(s1 + s2)
#HelloWorld
n1 = '100'
n2 = '200'
print(n1 + n2)
#100200

# 변수 삭제 del 사용
x = 10
# del x
print(x)
#Error

# 값이 들어있지 않은 빈 변수를 만들 때는 None을 할당
x = None
print(x)
#None

# 변수명 규칙
# 영문자[소문자 (a ~ z) 또는 대문자 (A ~ Z)], 한글, 숫자(0~9), 밑줄문자(_)로 사용하여 선언한다. 단 숫자로 시작하지 않는다.
# 예) Python_1 (○), 1_Python(×)
# 중간에 공백을 포함할 수 없다. 
# 두개 이상의 단어를 사용할 경우에는 밑줄로 연결한다.
# 예) Final_Exam (○), Final Exam (×)
# 대문자와 소문자가 구분된다.
# 예) Security와 security는 다른 변수이다.
# 파이썬의 예약어(keyword)와 함수이름은 사용할 수 없다.
# 예) if, else, for, while, print 등
# 의미 있는 단어로 표기하는 것이 좋다.
# 예) Department_Name (○), a, b (×)
# !, @, #, $, %, & 등 특수 기호는 식별자에서 사용할 수 없다.

# 예약어
# 파이썬이 내부적으로 사용하는 예약어는 변수의 이름으로 사용할 수 없다. 예약어를 사용하여 변수를 생성하면 오류가 발생한다. 

# 파이썬의 예약어 확인
import keyword
keyword.kwlist
print(keyword.kwlist)
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
# 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
# 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 자료형
# 변수에 저장되는 데이터 타입
# int, float, str, bool
# 파이썬 변수는 어떤 종류의 자료형도 저장이 가능
# 다른 언어는 변수를 선언할 때 자료형을 결정하고 반드시 같은 자료형 데이터만 저장이 가능함

# type() 함수
x = 10
print(type(x))
#<class 'int'>
y = "HelloWolrld"
print(type(y))
#<class 'str'>

# 정수 자료형
# 자연수를 포함해 양의 정수, 음의 정수, 숫자 0의 값을 소수점 없이 입력된 수
# 사람은 10진수를 사용하지만, 컴퓨터 내부적으로는 0, 1 밖에 없는 2진수를 사용하기 때문에, 
# 2진수를 숫자 3개씩 묶어서 표현하는 8진수, 
# 2진수 숫자 4개씩 묶어서 표현하는 16진수를 사용하는 일도 종종 있다 

# 10진수
a = 10
print(type(a))
#<class 'int'>

# 16진수
# 숫자 앞에 숫자 0과 알파벳 x를 붙여 0x 또는 0X
a = 0xFA
print(a)
# 250

# 8진수
# 숫자 앞에 숫자 0과 알파벳 o를 붙여 0o 또는 0O
a = 0o123
print(a)
#83

# 2진수
# 숫자 앞에 숫자 0과 알파벳 b를 붙여 0b 또는 0B
a = 0b0101
print(a)
#5

# 실생활에서는 큰 수를 알아보기 쉽도록 세자리마다 콤마(,)를 붙임
# 파이썬에서는 콤마대신 밑줄(_)을 붙여 표시할 수 있다.
print(100_000_000)
#100000000

# 숫자 0을 다른 숫자 앞에 넣으면 오류

# 실수 자료형
# 소수점이 포함된 숫자를 의미. 부동소수점 이라고도 함
a = 1.2
print(type(a))
#<class 'float'>
a = -1.2
print(type(a))
#<class 'float'>

# 컴퓨터식 지수 표현 방식
# 3.23E8 -> 3.23*10의8제곱
# 23e-10 -> 23*10-10의8제곱
b = 3.23E8
print(b)
#323000000.0
c = 23e-10
print(c)
#2.3e-09

# 문자열(String, str) 자료형
# 문자, 단어, 숫자 등으로 구성된 문자들의 집합으로 큰따옴표(“) 또는 작은따옴표(;)로 둘러싸서 표현
a = "Hello"
print(type(a))
#<class 'str'>
b = '123'
print(type(b))
#<class 'str'>

#부울(Boolean, bool) 자료형
# 참과 거짓을 나타내는 자료형. ‘True’나 ‘False’ 값만 가질 수 있다. 첫 문자는 항상 대문자로 사용해야 함
# true, false 으로 사용하면 안됨
# 단독으로 사용되기 보다는 조건문이나 반복문에서 사용
a = True
print(type(a))
#<class 'bool'>
b = False
print(type(b))
#<class 'bool'>
a = (100 < 100)
print(a)
#False
b = (100 == 100)
print(b)
#True

# None은 비어 있는 값
# 다른 언어의 ‘null’과 유사한 개념
# 변수를 선언할 때 값을 대입하여야 하는데 아무것도 대입하지 않고 선언하고자 할 때 사용
a = None
print(a)
#None
print(type(a))
#<class 'NoneType'>

# 반지름이 5.0인 원의 면적을 계산하는 프로그램을 작성하세요.
# 원의 면적 = 3.141592 * 반지름 * 반지름
반지름 = 5.0
원의_면적 = 3.141592 * 반지름**2
print("원의 면적은", 원의_면적, "입니다.")
#원의 면적은 78.5398 입니다.

# 체중(kg)과 키(m)를 변수에 넣어서 신체질량지수 BMI 를 계산하여 출력하는 프로그램을 작성하세요
# BMI=𝑤/ℎ의제곱2
체중 = 82.5
키 = 1.76
bmi = 체중 / 키**2
print("BMI는", bmi)
#BMI는 26.633522727272727

# 부울값 이해하기
b1 = True
b2 = False
print(b1)
#True
print(b2)
#False
print(3<4)
#True
print(3>4)
#False