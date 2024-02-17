month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

month_number = int(input("Digite um número entre 1 e 12: "))

if 1 <= month_number <= 12:
    month_name = month[month_number]
    print(month_name.capitalize())
else:
    print("Número de mês inválido! O número deve estar entre 1 e 12.")    