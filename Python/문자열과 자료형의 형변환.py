# 문자열 : 문자들의 연속된 모음
# 컴퓨터는 사실 0과 1 밖에 모르니 모든 것을 내부적으로숫자로 처리함. 그래서 숫자가 더 중요
# 하지만 사람은 주로 글자(텍스트, Text)로 정보를 표현하고 이해함. 그래서 프로그래밍에서 문자열(String) 처리가 무척 중요함

# 문자열 만드는 법
# 큰따옴표(“…”)나 작은따옴표('...') 로 텍스트를 감싸면 문자열이 된다.

# 문자열 문법 오류
# s = Hello
# 따옴표가 없어지면 변수로 인식이 됨

# 따옴표 출력
s = "그가 '좋아' 라고 답했다." # '그가 '좋아'라고 답했다.' 라고 하면 Error.
print(s) 
#그가 '좋아' 라고 답했다.

# 백슬러시(\)
# 문자열에 백슬러시(\)를 사용하면 문자열 예외처리나 특수한 기능 추가도 가능함 
s = '그가 \'좋아\' 라고 답했다.'
print(s) 
#그가 '좋아' 라고 답했다.

# 이스케이프 문자
# 이스케이프 시퀀스(escape sequence)를 따르는 문자들로서 다음 문자가 특수 문자임을 알리는 백슬래시(\)를 사용
print("Hello \nWorld") # 문자열 안에서 줄 바꿈
#Hello
#World
print("Hello \tWorld") # 문자열 사이에 탭 간격
#Hello   World
print("Hello \\World") # 문자 \ 그대로 표현할 때 사용
#Hello \World
print("Hello \bWorld") # 백스페이스
#HelloWorld
print("Hello \vWorld") # 수직 탭
#Hello
#     World

print("\u0061")  # 유니코드 0061값에 해당되는 문자
#a

#문자열 포맷팅
#문자열 안의 특정 위치에 원하는 값을 삽입하고자 할 때 문자열 포맷팅을 사용
name = "홍길동"
print("제 이름은 %s 입니다." %name) 
#제 이름은 홍길동 입니다.
age = 22
print("나이는 %d살 입니다." %age) 
#나이는 22살 입니다.
height = 176.5
print("키는 %fcm 입니다." %height) 
#키는 176.500000cm 입니다.
print("키는 %.1fcm 입니다." %height) # %f 자리수 정하기 
#키는 176.5cm 입니다.

# 미리 포맷을 만들어 놓고 변수와 같이 사용할 수도 있습니다. 
msg = "현재 시간은 %s 입니다."
time = "12:00pm"
print(msg %time) 
#현재 시간은 12:00pm 입니다.

# 하나 이상의 값은 괄호 사용
print("전공은 %s이고 현재 %d학년입니다." %("컴퓨터", 1)) 
#전공은 컴퓨터이고 현재 1학년입니다.

# 미리 만든 포맷도 가능
msg = "오늘은 %s월 %s일입니다."
print(msg %(5, 15)) 
#오늘은 5월 15일입니다.

# 문자열 더하기
# 연산자 +를 이용해서 문자열 연결
print('컴퓨터' + '공학과') # 컴퓨터공학과
first = "컴퓨터"
print(first + "공학과") # 컴퓨터공학과

# 문자열 반복
# 문자열 곱하기
# 연산자 *를 이용해서 문자열 반복 가능
star = "*"
print(star * 50) 
#**************************************************
s1 = '컴퓨터'
s2 = '공학과'
s3 = (s1 + s2 + '!! ')*3 # (컴퓨터공학과!! )
print(s3) 
#컴퓨터공학과!! 컴퓨터공학과!! 컴퓨터공학과!!

# 인덱싱
# 문자열 중에서 하나의 문자를 추출하려고 할 때 사용
# 문자열의 각 문자마다 번호가 매겨지는데 이것을 인덱스 번호
# 인덱스 번호를 가지고 문자열의 특정 위치의 문자를 접근
# 양수인덱스 번호는 0번부터 시작
# 왼쪽에서 오른쪽으로 번호가 매겨진다.
# 음수인덱스는 가장 오른쪽이 -1
# 오른쪽에서 왼쪽으로 번호가 매겨진다.
s = 'Hello' #양수인덱스 0,1,2,3,4 음수인덱스 -5,-4,-3,-2,-1
print(s[0]) 
#H
print(s[4]) 
#o
print(s[-1])
#o

s = 'Hello'
# s[0] = 'K' 
# 한번 작성된 인덱스 문자는 변경 할 수 없다. Error.

# 슬라이싱
# 문자열에서 특정 구간을 추출  때  사용
# 인덱스 번호 구간을 [시작 번호 : 끝 번호]로 선언
# 끝 번호는 포함하지 않고 그전 까지 추출함  
s = 'Hello World'
print(s[0:2])  # 0~1
#He 
print(s[0:5])  # 0~4
#Hello 
print(s[5:8])  # 5~7
#Wo
print(s[6:11]) # 6~10
#World 

# 시작 번호, 끝번호도 생략 가능
# 시작번호는 처음, 끝번호는 마지막 인덱스로 동작
s = 'Hello World'
print(s[:5]) # 0~4
#Hello 
print(s[6:]) # 7~
#World 
print(s[:]) 
#Hello World 

# 문자열로 날짜와 관련된 Raw Data(미가공 데이터)가 있습니다. 이 문자열을 나누어서 다음과 같이 출력한 프로그램을 작성해 보세요.
#2021년 05월 14일 Friday
s = '20210514Friday'
year = s[:4] 
month = s[4:6]
day = s[6:8]
week = s[8:]
date = year + '년 ' + month + '월 ' + day + '일 ' + week
print(date) 
#2021년 05월 14일 Friday

# 변수에 입력된 문자열 중 틀린 철자가 있습니다. 슬라이싱을 사용해서 수정된 새로운 문자열을 만들어 보세요.
s = "wokld" # world가 맞음
front = s[:2] #wo
back = s[3:] #ld
new = front + 'r' + back
print(new)
#world


#문자열 함수
# 문자열 처리는 상당히 중요하고 자주하는 일
# 그래서 파이썬에서는 많은 라이브러리 함수(내장함수)를 기본적으로 제공하고 있음

# count
# 문자열에서 특정 문자의 개수를 카운트 할 때 사용
s = 'Hello World'
print(s.count('l')) 
#3
#l은 3개 있음
print(s.count('w')) 
#0
#대소문자 구분함

#find()
# 특정 문자의 위치를 파악하여 위치 값(인덱스)을 반환해주는 함수
s = 'Hello World'
print(s.find('H'))
#0
print(s.find('o'))
#4
print(s.find('World'))
#6
print(s.find('p'))
#-1
#없으면 -1 반환한다.

#index()
# 특정 문자의 위치 값을 반환해 주는 함수
# find()함수와는 달리 찾고자 하는 특정 문자가 없으면 오류가 발생함
s = 'Hello World'
print(s.index('H')) 
#0
print(s.index('Wo'))
#6
# print(s.index('P')) P가 없어서 오류남

# strip()
# 양쪽 공백 제거
s = '   Hello   '
print(s.strip())
#Hello

# lstrip 
# # 왼쪽 공백 제거
print(s.lstrip())
#Hello

# rstrip
# 오른쪽 공백 제거
print(s.rstrip())
#   Hello 

# upper() : 문자열의 알파벳을 모두 대문자로 변환
# lower() : 문자열의 알파벳을 모두 소문자로 변환
s = 'Hello World'
print(s.upper())
#HELLO WORLD
print(s.lower())
#hello world

# join()
# 구분자를 사용하여 문자열의 각각 문자 사이에 삽입
s = 'Hello'
print('/'.join(s))
#H/e/l/l/o
sep = ' - '
print(sep.join('ABCDE'))
#A - B - C - D - E

# replace(인수1, 인수2) 
# 문자열에서 인수1 문자열을 인수2 문자열로 치환하는 함수
s = 'Hello World'
print(s.replace('o', 'a')) # o를 a로 바꿔라
#Hella Warld
print(s.replace('World', 'Python')) # World를 Python로 바꿔라
#Hello Python

# split(공백 또는 구분자) 
# 문자열을 공백 또는 구분자로 나누는 함수
s = 'Hello World'
print(s.split()) # 공백으로 나누기
#['Hello', 'World']
s = 'www.nrf.re.kr'
print(s.split('.')) # 구분자(여기서는 '.')로 나누기
#['www', 'nrf', 're', 'kr']

# format()
# { } 포맷 코드를 사용하여 포맷팅 문자열 내용을 나중에 바꿔줄 수 있음
s = 'Hello {}'
print(s.format('World'))
#Hello World
print(s.format('Python'))
#Hello Python

# {인덱스} 포맷 사용하면 순서도 변경 가능
s = 'Hello {0} {1}'
print(s.format('Wolrd', 'Python'))
#Hello Wolrd Python
s = 'Hello {1} {0}'
print(s.format('World', 'Python'))
#Hello Python World

# {이름} 포맷 사용하면 { } 내에 이름 지정 가능
s = 'Hello {s1} {s2}'
print(s.format(s2= 'World', s1= 'Python'))
#Hello Python World

# len() 
# 문자열의 길이를 반환
s = 'Hello'
print(len(s))
#5
col = [1,2,3,4]
print(len(col)) # 자료형의 갯수만 나옴
#4

#chr()
# 유니코드 값을 입력 받아 해당하는 문자를 반환
print(chr(97)) # 10진수 유니코드 값
#a
print(chr(0x3131)) #16진수 유니코드 값
#ㄱ

# 문자를 입력 받아 유니코드 값을 반환
print(ord('A')) # a의 유니코드 값
#65
print(ord('ㄱ')) # ㄱ의 유니코드 값
#12593

# hex()
# 입력 받은 정수를 16진수로 변환하여 반환
print(hex(12593))
#0x3131
print(hex(97))
#0x61

# oct()
# 입력 받은 정수를 8진수로 변환하여 반환
print(oct(9))
#0o11
print(oct(16))
#0o20

# 자료형 변환
# print(10+'10') Error. 자료형이 다르면 연산이 되지 않는다.
# 자료형을 같도록 만들어야 함
# 형변환 함수를 사용하여 자료형을 통일해야 한다
print(10+int('10')) #'10'을 정수로 바꿔주는 함수 사용
#20
print(str(10)+'10') # 10을 문자열로 바꿔주는 함수 사용
#1010

#int()
# 실수, 문자열, 계산식을 강제로 정수로 변환해주는 함수
print(int(3.14159))
#3
print(int(7 / 3))
#2
print(int('2000'))
#2000

# 변환이 불가능한 자료형이 들어오면 에러
# print(int('a')) Error

# int() 함수와 같이 쓰기
a = int(input("정수를 입력하시오: ")) # 10
print(a+10)
#20

# float()
# 정수, 문자열, 계산식을 실수로 강제로 변환해주는 함수
print(float(3))
#3.0
print(float(6/3))
#2.0
print(float('2000'))
#2000.0
print(float('3.14159'))
#3.14159

# input() 함수와 같이 쓰기
a = float(input("정수를 입력하시오: ")) # 10
print(a+10)
#20.0

# str
# 정수나 실수를 강제로 문자열로 변환해주는 함수 
# 정수나 실수를 문자열과 연산하면 오류 발생하므로 사용
score = 100
print(str(score) + "점 입니다.")
#100점 입니다.