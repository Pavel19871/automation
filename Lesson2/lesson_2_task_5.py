month = int(input("Ввести число месяца (в диапазоне от 1 до 12): "))

def month_to_season(month):
        if month in [12, 1, 2]:
            print(f"номер месяца {month} соответствует сезону Зимы")
        elif month in [3, 4, 5]:
            print(f"номер месяца {month} соответствует сезону Весны")
        elif month in [6, 7, 8]:
             print(f"номер месяца {month} соответствует сезону Лета")
        elif month in [9, 10, 11]:
             print(f"номер месяца {month} соответствует сезону Осени")
        else:
             print("Вы ввели число, выходящее за пределы диапазона. Попробуйте.")
             month = int(input("Ввести число месяца (в диапазоне от 1 до 12): "))
        
month_to_season(month)