from random import randint  # random 모듈에서 randint 함수 가져오기

# 파이썬 카지노 만들기
""" 
1. 컴퓨터가 숫자 하나 선택
2. user도 숫자 하나 선택
3. user가 숫자를 정확하게 맞추면 이기고, 아니면 지는 게임
"""

user_choice = int(input("Choose number 1 ~ 50"))
# pc_choice = 50
pc_choice = randint(1, 10)

if user_choice == pc_choice:
    print("You Win")
elif user_choice > pc_choice:
    print("더 작은 값, Computer chose", pc_choice)
else:
    print("더 큰 값! Computer chose", pc_choice)
