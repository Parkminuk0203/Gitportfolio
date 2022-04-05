# 따옴표 출력
s = "그가 '좋아' 라고 답했다." # '그가 '좋아'라고 답했다.' 라고 하면 Error.
print(s) #그가 '좋아' 라고 답했다.

# 백슬러시(\)
s = '그가 \'좋아\' 라고 답했다.'
print(s) #그가 '좋아' 라고 답했다.

# 이스케이프 문자
print("Hello \nWorld") 
# Hello
# World
print("Hello \tWorld") # Hello   World
print("Hello \\World") # Hello \World
print("Hello \bWorld") # HelloWorld
print("Hello \vWorld")
# Hello
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
print(s[0:2]) # He
print(s[0:5]) # Hello
print(s[5:8]) #  Wo
print(s[6:11]) # World

