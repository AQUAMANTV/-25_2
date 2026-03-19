money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months_count = 0
current_budget = money_capital

while True:

    current_spend = spend * ((1 + increase) ** months_count)

    total_monthly_budget = current_budget + salary


    if total_monthly_budget >= current_spend:
        current_budget += salary - current_spend
        months_count += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months_count)