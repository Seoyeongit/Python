
num1=int(input("첫 번째 숫자 입력 : "))        # 두 개의 서로 다른 숫자를 정수로 입력 
num2=int(input("두 번째 숫자 입력 : "))        

if num1%2==0 and num2%2==0 :               # 관계,논리 연산자를 사용하여 비교 
    print("두 숫자가 모두 짝수입니다")
             
elif num1%2==1 and num2%2==1 :              # 다시 조건을 제시하여 비교 
    print("두 숫자가 모두 홀수입니다")

else :
    print("짝수 홀수가 섞여있습니다")             
          
    
