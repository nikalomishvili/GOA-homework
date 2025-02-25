
we = float(input("Введите вес (в кг): "))
he = float(input("Введите рост (в метрах): "))


abc = we / (he ** 2)


if abc < 18.5:
    ca = "Underweight"
elif 18.5 <= abc < 25:
    ca = "Normal"
elif 25 <= abc < 30:
    ca = "Overweight"
else:
    ca = "Obesity"


print(ca)