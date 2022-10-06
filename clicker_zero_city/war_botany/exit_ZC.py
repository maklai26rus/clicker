import psutil


def exit_zc():
    """Закрытия процеса ZC.exe """

    for process in (process for process in psutil.process_iter() if process.name() == "ZC.exe"):
        process.kill()


def exit_mgl():
    """Закрытия процеса ZC.exe """

    for process in (process for process in psutil.process_iter() if process.name() == "MGL.exe"):
        process.kill()
