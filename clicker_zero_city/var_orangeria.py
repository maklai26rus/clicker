import pyautogui
import time

try:
    import easyocr
except UserWarning:
    print("ошибка модуля")

global_map = "png/global_maps.PNG"
kater = "png/kater.PNG"
stop = "png/stop.PNG"
orang = "png/orang.PNG"
battle = 'png/battle.PNG'
battle_next = 'png/battle_next.PNG'
update = 'png/update.PNG'
my_strength = 3400000

reader = easyocr.Reader(['ru'])


def time_game(func):
    def other_func():
        time.sleep(5)
        func()
        return func

    return other_func


def start_var_orangeria():
    """Запуск скрипта"""
    global_maps()


@time_game
def global_maps():
    """
    Переходим на глобальную карту для поиска  оранжереи
    :return:
    """
    click = pyautogui.locateOnScreen(global_map, confidence=0.5)
    if click:
        pyautogui.click(click)
    time.sleep(1)

    if greenhouse_search():
        pass
    else:
        boat_search()
        greenhouse_search()

    update_map()
    get_enemy()


def boat_search():
    """
    Ищем на карте катер и привязываемся к нему что бы перетащить мышкку
    :return:
    """
    click = pyautogui.locateOnScreen(kater, confidence=0.4)
    if click:
        pyautogui.click(click)
        pyautogui.dragTo(100, 0, 1, button='left')


def update_map():
    # click = pyautogui.locateOnScreen(update, confidence=0.7)
    click = pyautogui.locateOnScreen(update, confidence=0.9)
    # pyautogui.click(click)
    pyautogui.click(click)
    time.sleep(1)


def greenhouse_search():
    """
    Определяем на карте оранжерею
    :return:
    """
    click = pyautogui.locateOnScreen(orang, confidence=0.5)
    if click:
        pyautogui.click(click)
        time.sleep(10)


def get_enemy():
    """
    Определение пративника по его силе.
    в my_strength указана максимальная сила для нападения
    """
    number_temp = 1
    path_temp = f'png/temp/{number_temp}.png'
    battle_click = list(pyautogui.locateAllOnScreen(battle, confidence=0.9, grayscale=True))

    for enemy in battle_click:
        pyautogui.screenshot(path_temp, region=(enemy.left - 390, enemy.top, enemy.width + 130, enemy.height + 10))
        time.sleep(0.1)
        enemy_strength = reader.readtext(path_temp, detail=0)
        es_int = int(enemy_strength[1].replace(' ', ''))
        if my_strength >= es_int:
            center = pyautogui.center(enemy)
            pyautogui.click(center)
            time.sleep(0.2)

            start_battle_orangeria()

            time.sleep(5)

        number_temp += 1


def start_battle_orangeria():
    """Определяет если активна кнопка или выйти с выбора """
    click = pyautogui.locateOnScreen(battle_next, confidence=0.6)
    if click:
        pyautogui.click(click)
        time.sleep(4)

        stop_battle()

        time.sleep(20)
        pyautogui.press('esc')

    else:
        pyautogui.press('esc')


def stop_battle():
    """
    Если энергия закончилась
    кликер закрывает окно
    """
    battle_stop = pyautogui.locateOnScreen(stop, confidence=0.6)
    if battle_stop:
        time.sleep(0.1)
        pyautogui.press('esc')


