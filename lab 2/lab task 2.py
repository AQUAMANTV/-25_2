salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0
current_spend = spend

for month in range(months):

    if month > 0:
        current_spend *= (1 + increase)


    deficit = max(0, current_spend - salary)

    money_capital += deficit

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))