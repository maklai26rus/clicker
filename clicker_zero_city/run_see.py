from actions_see import main_actions_see
from run_video import watch_ads

if __name__ == '__main__':
    try:
        main_actions_see()
    except KeyboardInterrupt:
        print('Закрытия программы')
