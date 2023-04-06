
kor=int(input("국어 점수를 입력 : "))             # 3과목 점수를 입력
eng=int(input("영어 점수를 입력 : "))
math=int(input("수학 점수를 입력 : "))

avg=(kor+eng+math)/3                          # 평균을 구한다

if avg >= 95 :
    # {} 안에는 점수가 들어감
    print("당신의 평균은 {}점입니다.".format(avg))  # 조건이 참일 때 수행하는 블록
    print("축하합니다. A+입니다")

print("감사합니다")                              # 조건 만족여부와 상관없이 출력
