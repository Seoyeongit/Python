
score=int(input("점수를 입력하세요 : "))        #정수로 입력

if score >= 90 :                  
    print("A학점입니다")
    
elif score >= 80 :                                        #조건이 거짓일 경우 다시 조건을 검사 
    print("B학점입니다")
    
elif score >= 70 :
    print("C학점입니다")
    
elif score >= 60 :
    print("D학점입니다")
    
else :                             
    print("F학점입니다")                                 #마지막 조건이 거짓일 경우 수행 

          
