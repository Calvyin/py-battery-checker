import psutil as ps
from win10toast import ToastNotifier


toast = ToastNotifier()


def print_bat_life():
    bat = ps.sensors_battery()  # function returns bat.percent, bat.secsleft, bat.power_plugged
    mm, ss = divmod(bat.secsleft, 60)
    hh, mm = divmod(mm, 60)
    print(f"Battery percentage: {bat.percent} Battery life: {hh}:{mm}")


def bat_check(enabled):
    while enabled:
        global notified
        global charged
        bat = ps.sensors_battery()  # function returns bat.percent, bat.secsleft, bat.power_plugged
        charged = False
        while charged is False:
            if bat.percent == 60:
                toast.show_toast(
                    "Warning",
                    "Battery has reached 60%",
                    duration=20,
                    icon_path="icon.ico",
                    threaded=True,
                )
                notified = True
                charged = True
            else:
                pass
        if (notified is True) and (bat.power_plugged is False) and (bat.percent < 60):
            notified = False
            charged = False

