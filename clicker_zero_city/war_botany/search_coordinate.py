import pyautogui


def search_coordinate(path_rooms):
    """Принимает путь к директории и перебирает все файлы в ней.
        Если в момент запуска была найдена точка то воозращает координату ее ддля дальнейшего действия

    return: Возращает найденую координату
    """
    coordinate = None
    for pr in path_rooms:
        click = pyautogui.locateOnScreen(pr, confidence=0.65)
        if click:
            coordinate = click
            break
    return coordinate


# def search_coordinate_ad(path_rooms_png) -> list:
#     """Принимает путь к директории и перебирает все файлы в ней.
#         Если в момент запуска была найдена точка то воозращает координату ее ддля дальнейшего действия
#
#     return: Возращает найденую координату
#     """
#     return pyautogui.locateOnScreen(path_rooms_png, confidence=0.7)
