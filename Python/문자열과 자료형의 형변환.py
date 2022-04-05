#따옴표 출력
s = "그가 '좋아' 라고 답했다." # '그가 '좋아'라고 답했다.' 라고 하면 Error.
print(s) #그가 '좋아' 라고 답했다.

#백슬러시(\)
s = '그가 \'좋아\' 라고 답했다.'
print(s) #그가 '좋아' 라고 답했다.

#이스케이프 문자
print("Hello \nWorld") 
#Hello
#World
print("Hello \tWorld") 
#Hello   World
print("Hello \\World") 
#Hello \World
print("Hello \bWorld") 
#HelloWorld
print("Hello \vWorld")
#Hello
#      World
print("\u0061") # a

# 문자열 포맷팅
name = "홍길동"
print("제 이름은 %s 입니다." %name) # 제 이름은 홍길동 입니다.

age = 22
print("나이는 %d살 입니다." %age) # 나이는 22살 입니다.

height = 176.5
print("키는 %fcm 입니다." %height) # 키는 176.500000cm 입니다.
print("키는 %.1fcm 입니다." %height) # 키는 176.5cm 입니다.

msg = "현재 시간은 %s 입니다."
time = "12:00pm"
print(msg %time) # 현재 시간은 12:00pm 입니다.

print("전공은 %s이고 현재 %d학년입니다." %("컴퓨터", 1)) # 전공은 컴퓨터이고 현재 1학년입니다.

msg = "오늘은 %s월 %s일입니다."
print(msg % (5, 15)) # 오늘은 5월 15일입니다.

print('컴퓨터' + '공학과') # 컴퓨터공학과
first = "컴퓨터"
print(first + "공학과") # 컴퓨터공학과

# 문자열 반복
star = "*"
print(star * 50) # **************************************************

s1 = '컴퓨터'
s2 = '공학과'
s3 = (s1 + s2 + '!! ') * 3
print(s3) # 컴퓨터공학과!! 컴퓨터공학과!! 컴퓨터공학과!!

# 인덱싱
# 인덱스 번호는 0번부터 시작
# 파이썬만 음수 인덱스 가능함
s = 'Hello' # 양수인덱스 0,1,2,3,4 음수인덱스 -5,-4,-3,-2,-1
print(s[0]) # H
print(s[4]) # o
print(s[-1]) # o

s = 'Hello'
# s[0] = 'K' 인덱스 문자는 변경 할 수 없다. Error.

# 슬라이싱
s = 'Hello World'
print(s[0:2]) # He 0~1
print(s[0:5]) # Hello 0~4
print(s[5:8]) #  Wo 5~7
print(s[6:11]) # World 7~10

# 시작 번호, 끝번호도 생략 가능
s = 'Hello World'
print(s[:5]) # Hello 0~4
print(s[6:]) # World 7~
print(s[:]) # Hello World 

s = '20210514Friday'

year = s[:4] 
month = s[4:6]
day = s[6:8]
week = s[8:]
date = year + '년 ' + month + '월 ' + day + '일 ' + week
print(date) # 2021년 05월 14일 Friday

#문자열 함수
#count
s = 'Hello World'
print(s.count('l')) 
#3
#l은 3개 있음
print(s.count('w')) 
#0
#대소문자 구분함

#find()
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
print(s.index('H')) 
#0
print(s.index('Wo'))
#6
#print(s.index('P')) P가 없어서 오류남

#strip()
s = '   Hello   '
print(s.strip())
#Hello 양쪽 공백 제거
print(s.lstrip())
#Hello 왼쪽 공백 제거
print(s.rstrip())
#   Hello 오른쪽 공백 제거

s = 'Hello World'
print(s.upper())
#HELLO WORLD 문자열의 알파벳을 모두 대문자로 변환
print(s.lower())
#hello world 문자열의 알파벳을 모두 소문자로 변환

#join()
s = 'Hello'
print('/'.join(s))
#H/e/l/l/o
sep = ' - '
print(sep.join('ABCDE'))
#A - B - C - D - E

#replace() 함수
s = 'Hello World'
print(s.replace('o', 'a')) #o를 a로 바꿔라
#Hella Warld
print(s.replace('World', 'Python')) #World를 Python로 바꿔라
#Hello Python

#split(공백 또는 구분자)
s = 'Hello World'
print(s.split()) # 공백으로 나누기
#['Hello', 'World']
s = 'www.nrf.re.kr'
print(s.split('.')) # 구분자(여기서는 '.')로 나누기
#['www', 'nrf', 're', 'kr']

#format()
s = 'Hello {}'
print(s.format('World'))
#Hello World
print(s.format('Python'))
#Hello Python

s = 'Hello {0} {1}'
print(s.format('Wolrd', 'Python'))
#Hello Wolrd Python
s = 'Hello {1} {0}'
print(s.format('World', 'Python'))
#Hello Python World
s = 'Hello {s1} {s2}'
print(s.format(s2= 'World', s1= 'Python'))
#Hello Python World