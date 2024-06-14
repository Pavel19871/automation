year_as_a_line = input("Выбор года:")
year = int(year_as_a_line)


def is_year_leap():
    if year % 4 == 0:
        print("Year", year, ":", True)
    else:
        print("Year", year, ":", False)
is_year_leap()            