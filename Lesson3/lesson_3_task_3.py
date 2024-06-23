
from address import address
from mailing import mailing

to_address = address
from_address = address
to_address = 457040, "г. Южноуральск", "ул. Советской Армии", 31, 10
from_address = 457000, "г. Челябинск", "ул. Кожезаводская", 39, 45

sending = mailing
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

