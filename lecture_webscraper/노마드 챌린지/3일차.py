# 👇🏻 YOUR CODE 👇🏻:

# /YOUR CODE


# 1. 연간 매출
def get_yearly_revenue(monthly_revenue):
    revenue_for_a_year = monthly_revenue * 12
    return revenue_for_a_year


# 2. 연간 비용
def get_yearly_expenses(monthly_expenses):
    expenses_for_a_year = monthly_expenses * 12
    return expenses_for_a_year


# 3. 세금 계산
def get_tax_amount(profit):
    if profit > 100000:
        tax_amount = profit * 0.25
    else:
        tax_amount = profit * 0.15

    return tax_amount


# 4. 세액 공제 적용
def apply_tax_credits(tax_amount, tax_credits):
    amount_to_discount = tax_amount * (1 - tax_credits)
    return amount_to_discount


# BLUEPRINT | DONT EDIT

monthly_revenue = 5500000  # 월간 매출
monthly_expenses = 2700000  # 월간 비용
tax_credits = 0.01  # 세액 공제율


yearly_revenue = get_yearly_revenue(monthly_revenue)  # 연간 매출
yearly_expenses = get_yearly_expenses(monthly_expenses)  # 연간 비용

profit = yearly_revenue - yearly_expenses  # 이익

tax_amount = get_tax_amount(profit)  # 세금 금액

final_tax_amount = tax_amount - apply_tax_credits(tax_amount, tax_credits)

print(f"Your tax bill is: ${final_tax_amount}")


# /BLUEPRINT
