
from address import Address
from mailing import Mailing

to_address = Address(457040, "г. Южноуральск", "ул. Советской Армии", 31, 10)
from_address = Address(457000, "г. Челябинск", "ул. Кожезаводская", 39, 45)
to_address = 457040, "г. Южноуральск", "ул. Советской Армии", 31, 10
from_address = 457000, "г. Челябинск", "ул. Кожезаводская", 39, 45

sending = Mailing
sending(to_address, from_address, 2000, 9534)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)

