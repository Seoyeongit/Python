print("파이썬 프로그래밍을 시작합니다")

a = 10
b = 20
c = a + b
print(c)

# 들여쓰기 예제
x = int(input()) # x : 입력받는 int(정수)
if(x%2) == 1:
    print("홀수이다")
else:
    print("짝수이다")

# 1-10중에서 홀수만 출력 한다
num = 1 # num은 1~10범위의 숫자를 저장할 변수이다.
for num in range(1,11): 
    if num % 2 == 1: # num을 2로 나눌 때 나머지가 1인가?(짝수일 땐 0)
        print(num)

