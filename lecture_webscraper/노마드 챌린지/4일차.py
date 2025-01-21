# 1. 유저로부터 숫자 입력받기
# 2. 유저로부터 숫자 입력받기
# 3. 유저로부터 연산자 입력받기 +, -, * , /  또는 exit 입력시 끝냄
# 4. 3에서 입력받은 것으로 결과를 보내고 다시 1로 돌아감


game_on = True

while game_on:
    num1 = int(input("Choose a number : "))
    print(num1)
    num2 = int(input("Choose another one : "))
    print(num2)

    operation = input(
        "Choose an operation : Operation are: +, -, * or / . Write 'exit to finish"
    )
    if operation == "exit":
        game_on = False
    elif operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2)
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    else:
        print("연산자를 잘못 입력하셨습니다.")


""" 
4일차정답 코드
playing = True

while playing:
  a = int(input("Choose a number:\n"))
  b = int(input("Choose another one:\n"))
  operation = input(
      "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n"
  )

  if operation == "+":
    print("Result:", a + b)
  elif operation == "-":
    print("Result:", a - b)
  elif operation == "*":
    print("Result:", a * b)
  elif operation == "/":
    print("Result:", a / b)
  elif 'exit':
    playing = False
"""
