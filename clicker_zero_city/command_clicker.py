choosing_action = {"rooms": False, 'tablet': False}


def advertising_rooms():
    """
    Просмотр рекламы по комнатам
    """
    if choosing_action["rooms"]:
        shutdown_click()
        print(f"Выключение кликер реклама в комнатах")
    else:
        shutdown_click()
        choosing_action["rooms"] = True
        print(f"Включение кликер реклама в комнатах")


def advertising_tablet():
    """
    Просмотр рекламы в планшете
    """

    if choosing_action["tablet"]:
        shutdown_click()
        print(f"Выключение кликер реклама  в планшеты")
    else:
        shutdown_click()
        choosing_action["tablet"] = True
        print(f"Включение кликер реклама  в планшеты")


def shutdown_click():
    for k in choosing_action.keys():
        choosing_action[k] = False
