# 연산자 : 여러 식이나 값에 수학적. 논리적인 움직임을 지시하는 것.
# 피연산자 : 연산의 대상이 되는 것.

# 대입연산자 : 오른쪽 수식이나 변수의 값을 왼쪽 변수에 대입.
x = 10
print(x)
#10

# 10 = x # 안됨.

# 다중 할당
x = y = 100
print(x,y)
#100 100

# 동시 할당
n1, n2 = 100, 200
print(n1, n2)
#100 200

# 산술 연산자
# + 덧셈
# - 뺄셈
# * 곱셈
# / 나눗셈
# // 버림나눗셈(몫만 구함)
# % 나머지
# ** 거듭제곱
# 김기종 교수님이 3//10이였나 3%10 뭐라고 했더라 물어보기
print("김기종교수님=",3%10)

print(1+2)
#3
print(2-3)
#-1
print(3*4)
#12
print(8/4) # 나눗셈 값은 float로 반환되나?
#2.0
print(7//4)
#1
print(8//4)
#2

# 실수와 정수 사용되면
print(5.5+5)
#10.5
print(2-1.0)
#1.0
print(3.0*2)
#6.0
print(7.7+3.3)
#11.0
print("버림나눗셈=",5.5//3)
#버림나눗셈= 1.0
print("버림나눗셈=",4//2.0)
#버림나눗셈= 2.0
print("버림나눗셈=",4.5//2.5)
#버림나눗셈= 1.0

# 실수는 무한히 변경되는 상황이 있어서 경우에 따라 정확한 값이 아니라 근사치 저장.
print(4.3-2.7)
#1.5999999999999996
print(0.1+0.1+0.1)
#0.30000000000000004

# 정수를 입력받아 4칙연산 해보기
num = int(input("정수 입력: "))
print("10을 더하면", num + 10)
print("10을 빼면", num - 10)
print("10을 곱하면", num * 10)
print("10을 나누면", num / 10)

# 정수를 13을 입력받아
#13 나누기 5의 몫은 2
#13 나누기 5의 나머지는 3
# 출력하기
num = int(input("정수 입력: "))
print(num,"나누기 5의 몫은", num // 5)
print(num,"나누기 5의 나머지는", num % 5)

# 정수1은 12, 정수2는 6을 입력받아
#이들의 합은 18이고 곱은 72 입니다.
# 출력하기
num1 = int(input("정수1 입력: "))
num2 = int(input("정수2 입력: "))
print("이들의 합은", num1+num2, "이고 곱은", num1*num2)

# 실수 3.14159를 입력 받아
#입력한 실수는 3.14159 출력시키기
# 출력하기
num = float(input("실수 입력: "))
print("입력한 실수는", num)

# inch 변환
num = float(input("cm 입력: "))
print("인치로 변환하면", num/2.54, "inch 입니다.")

# 세개의 수를 입력받아 합계와 평균 계산
num1 = int(input("num1 입력: "))
num2 = int(input("num2 입력: "))
num3 = int(input("num3 입력: "))
print("합계는", num1+num2+num3, "이고 평균은 ", float((num1+num2+num3)/3), "입니다.") # 주의 할 점 항상 평균은 float로 계산

# 생년월일 입력받아 "년","월","일" 출력
#20121215
birth = str(input("생년월일 입력: "))
year = birth[:4]
month = birth[4:6]
day = birth[6:]
print(year+"년", month+"월", day+"일")

# 복합대입 연산자
# +=
# -=
# *=
# /=
# //=
# %=
# **=

a = 10
a = a + 1
print(a)
#11
a = 10
a += 1
print(a)
#11
num = 200
num -= 100
print(num)
#100
num *= 20
print(num)
#2000
num /= 2
print(num)
#1000.0

# 관계 연산자
# ==
# !=
# >
# <
# >=
# <=

a, b = 10, 20
print(a==b)
#False
print(a!=b)
#True
print(a>b)
#False
print(a<b)
#True
print(a>=b)
#False
print(a<=b)
#True

# 논리연산자
# and 양쪽 모두 참 일때 참
# or 한쪽이라도 참 일때 참
# not 참과 거짓을 뒤집음

print(10 == 10 and 5 == 6)
#False
print(10 == 10 and 5 != 6)
#True
a, b = 10, 0
print(a == b or a > b)
#True
# 숫자 0이나 None 값은 False, 그 외 숫자들은 True로 간주함
print(not a)
#False
print(not b)
#True

# 윤년 여부 구하기
year = int(input("연도 입력: "))
ans = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print("윤년 여부:",ans)

