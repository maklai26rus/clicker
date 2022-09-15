import pyautogui
import time

launcher = 'png/MGLauncher.PNG'
zero = 'png/Zero.PNG'
game = 'png/games.PNG'
menu = "png/menu.PNG"
tractor = "png/tractor.PNG"
tractor2 = "png/tractor2.PNG"
av = "png/AB.PNG"
next_av = "png/next.PNG"
unikal = "png/unikal.PNG"


def time_game(func):
    def other_func():
        time.sleep(5)
        func()
        return func

    return other_func


def start_var_av():
    """Запуск скрипта"""
    finding_shortcut()
    game_selection()
    run_game()
    closing_ads()
    ak_search()
    run_ab()
    ab_next()


def finding_shortcut():
    """Поисе ярлыка на рабочем столе"""
    click = pyautogui.locateOnScreen(launcher, confidence=0.8)
    pyautogui.doubleClick(click)


@time_game
def game_selection():
    """Выбор игры"""
    click = pyautogui.locateOnScreen(zero)
    pyautogui.doubleClick(click)


@time_game
def run_game():
    """
    Запуск игры
    :return:
    """
    click = pyautogui.locateOnScreen(game)
    pyautogui.click(click)


@time_game
def closing_ads():
    """Закрытия рекламы"""
    # click = pyautogui.locateOnScreen(X, confidence=0.8)
    unikal_click = pyautogui.locateOnScreen(unikal, confidence=0.8)
    print('Проверка на рекламу = ', unikal_click)
    if unikal_click:
        print('Закрытия рекламы')
        uc = pyautogui.center(unikal_click)
        pyautogui.click(uc)
        pyautogui.press('esc')
        time.sleep(10)
        closing_ads()


@time_game
def ak_search():
    """
    Поиск Альянтосовской комнаты
    выбор ее на главную
    :return:
    """
    click = pyautogui.locateOnScreen(tractor2, confidence=0.7)
    if click:
        center_click = pyautogui.center(click)
        pyautogui.click(center_click)
        # pyautogui.doubleClick(click)


@time_game
def run_ab():
    """
    Выбор АВ
    :return:
    """
    click = pyautogui.locateOnScreen(av, confidence=0.5)
    pyautogui.click(click)


@time_game
def ab_next():
    """
    Выбор АВ
    :return:
    """
    click = pyautogui.locateOnScreen(next_av, confidence=0.7)
    if click:
        print('Начала войны')
        pyautogui.click(click)
        time.sleep(0.01)
        pyautogui.press('esc')
    else:
        print("Война уже начата")
        pyautogui.press('esc')


# ak_search()