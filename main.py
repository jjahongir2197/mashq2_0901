def bir_yuz_ikki():
    my_dict = {
        1: "Balans",
        2: "Trafiklarni",
        3: "Qarz olish",
        4: "Daqiqalar",
        5: "Avto Qarz",
        0: "Chiqish"
    }
    print(my_dict)
    operatsiya = int(input('Operatsiya nomerini tanlang: '))

    if operatsiya in my_dict.keys():
        print(f"Siz {my_dict[operatsiya]} xizmatni tanladingiz")
    else:
        print("Siz noto'g'ri nomer kiritdingiz")

bir_yuz_ikki()
