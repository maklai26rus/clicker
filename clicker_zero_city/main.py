from clicker_zero_city.clan_war import clan_war
from game_openings import open_game
from war_orangeria import start_war_orangeria
import schedule
from clicker_zero_city.exit_ZC import exit_zc, exit_mgl


def run():
    exit_mgl()
    exit_zc()
    open_game()
    clan_war()
    start_war_orangeria()
    exit_zc()


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
