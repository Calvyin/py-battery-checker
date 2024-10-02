import psutil as ps
import plyer as pl
import time


def print_bat_life():
    bat = ps.sensors_battery()  # functions returns bat.percent, bat.secsleft, bat.power_plugged
    mm, ss = divmod(bat.secsleft, 60)
    hh, mm = divmod(mm, 60)
    print(f"Battery percentage: {bat.percent} Battery life: {hh}:{mm}")


def bat_check():
    bat = ps.sensors_battery()  # functions returns bat.percent, bat.secsleft, bat.power_plugged
    starttime = time.monotonic()
    charged = False
    while charged is False:
        time.sleep(120.0 - ((time.monotonic() - starttime) % 120.0))
        if bat.percent == 60:
            pl.notification.notify(title='Battery Status', message='Your laptop battery has reached 60%\nUnplug your '
                                                                   'charger', app_name='Battery checker', app_icon='',
                                   timeout=10, ticker='', toast=False, hints={})
            charged = True
        else:
            pass
