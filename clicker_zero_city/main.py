from clan_war import start_var_av
from var_orangeria import start_var_orangeria
import schedule


def run():
    start_var_av()
    start_var_orangeria()


def main():
    # schedule.every().seconds.do(start_var_av)
    # schedule.every(1).seconds.do(start_var_orangeria)
    # schedule.every().hour.do(run)
    run()
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
    # start_var_av()
    # start_var_orangeria()
