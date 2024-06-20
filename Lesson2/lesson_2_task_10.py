def bank(x, y):
    rate = 0.10
    sum_after_y_years = x * (1 + rate) ** y
    return sum_after_y_years

x = float(input("какую сумму вы бы хотели внести? "))
y = int(input("Сколько лет вы бы хотели хранить ваши инвестиции? "))

result = bank(x, y)
print(f"если вы положите ${x} на {y} лет, тогда на вашем счету будет ${result:.2f}")