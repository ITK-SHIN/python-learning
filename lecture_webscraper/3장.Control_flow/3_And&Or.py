# 음주 가능 나이 계산기 만들기

# 유용한 3가지 함수
""" 
[ built-in 함수 ]
1. input()  
    유저에게 입력을 받는 함수
        하나의 argument만 받는다.   
        유저가 답을 해야 프로그램이 종료된다. 
         유저가 입력한 값이 함수의 return 값 

2. type()
    변수의 type을 알려주는 함수
    
3. int()
    정수로 타입변환하는 함수
"""
age = int(input("How old are you?"))

print("user answer", age)

print(type(age))


if age < 18:
    print("You can't dring.")
elif age >= 18 and age <= 35:
    print("18 ~ 35")
elif age == 60 or age == 70:
    print("Birthday party")
elif age >= 120:
    print("You are Sun of God")
else:
    print("Go ahead")
