import modi
import time
import datetime
bundle = modi.MODI()
# 사용할 모듈을 불러옵니다.
bundle.modules
# 현재 연결 된 모듈을 확인합니다.
display = bundle.display[0]
# 연결된 디스플레이 모듈 중 1번째 디스플레이 모듈을 display 변수로 지정한다.

# 실제로는 display.text = “원하는 글자”로 구현하려고 했지만 럭스로보가 없어,
# print문을 사용한 점 양해부탁드리겠습니다.

while [True] : 
# 화면에 시간을 실시간으로 표시하기위해 무한 반복문 사용.
    now = datetime.datetime.now()
    print(now)
# 현재 날짜와 시간을 실시간으로 표시

library_year = int(input("사용 가능한 년도를 입력하여 주십시오. : "))
# 사용 가능한 년도 입력
library_month= int(input("사용 가능한 월을 입력하여 주십시오. : "))
# 사용 가능한 월 입력
library_day= int(input("사용 가능한 일수를 입력하여 주십시오. : "))
# 사용 가능한 일 입력
today = datetime.datetime.today()
end_day = datetime.datetime(library_year, library_month, library_day)
d_day = end_day - today
print(d_day)
# 현재까지 남은 도서관 사용일수를 확인 가능

i = 0
Warning = 4
# 최대 경고 횟수 설정
while i < Warning : 
# 경고 횟수가 4회가 될 때까지 마이크를 통해 db를 계속 체크
    decibel = int(input("사운드는 몇 db입니까: "))
# 반복되는 동안 db 계속 체크, 사운드 관련 모듈을 몰라 임시적으로 input으로 테스트
# 도서관 적정 decibel을 참고해 20으로 설정
    if decibel < 20 : 
# 만약에 decibel이 20 미만이면
        print("경고 횟수 :",i)
# 경고 횟수만 출력하라.
    elif decibel > 20 :
# 만약에 decibel이 20 초과이면
        print("적정 데시벨을 초과하였습니다.")
        i += 1
        print("경고 횟수 :",i)
# 경고문을 출력하고 i에 1을 더하여라.
    if i == Warning :
# 만약에 i와 Warning이 같으면
        print("경고 횟수를 초과하였습니다. 퇴출하여 주십시오.")
        break
print("경고 횟수 :",i)
# 퇴출문과 경고 횟수를 출력하고 조건반복문에서 빠져나와라.