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