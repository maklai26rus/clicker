choosing_action = {"rooms": False, 'tablet': False}


def advertising_rooms():
    if choosing_action["rooms"]:
        choosing_action["rooms"] = False
        print("Выключение кликер реклама в комнатах")
    else:
        choosing_action["rooms"] = True
        print("Включение кликер реклама в комнатах")


def advertising_tablet():
    if choosing_action["tablet"]:
        choosing_action["tablet"] = False
        print("Выключение кликер реклама  в планшеты")
    else:
        choosing_action["table"] = True
        print("Включение кликер реклама  в планшеты")
