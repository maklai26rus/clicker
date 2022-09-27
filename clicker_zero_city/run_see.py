from run_video import watch_ads

if __name__ == '__main__':
    try:
        watch_ads()
    except KeyboardInterrupt:
        print('Закрытия программы')
