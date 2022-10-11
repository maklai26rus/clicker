import time

import schedule

from war_botany.clan_war import clan_war
from war_botany.exit_ZC import exit_mgl, exit_zc
from war_botany.game_openings import open_game
from war_botany.war_orangeria import start_war_orangeria


def run():
    print(time.strftime('%d/%m/%Y %H:%M:%S'))
    exit_mgl()
    exit_zc()
    open_game()
    clan_war()
    start_war_orangeria()
    exit_zc()
    exit_mgl()


def main():
    # schedule.every().seconds.do(run)
    # schedule.every(1).seconds.do(start_var_orangeria)
    # run()
    schedule.every().hour.do(run)
    # schedule.every(1).minutes.do(run)
    # schedule.every(90).minutes.do(run)
    while True:
        schedule.run_pending()
        # print(schedule)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Выключение программы")
    except:
        exit_mgl()
        exit_zc()
