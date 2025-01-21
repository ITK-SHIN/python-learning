# 문자열 안에 변수 넣기
my_name = "sangwoo"
my_age = 28
my_color_eyes = "brown"

print(
    f"Hello I'm {my_name}, I have{my_age} years in the earth, {my_color_eyes} is my eye color"
)


# 쥬스 메이커 만들기

# 1. 주스를 만드는 함수 만들기
# 2. 주스에 얼음 추가하는 함수 만들기
# 3. 주스에 설탕 넣는 함수 만들기


# 1
def make_juice(fruit):
    return f"{fruit}+🥤"


# 2
def add_ice(juice):
    return f"{juice}+🧊"


# 3
def add_sugar(iced_juice):
    return f"{iced_juice}+🍬"


juice = make_juice("🍎")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)
