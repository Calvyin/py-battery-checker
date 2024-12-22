import psutil as ps
from win10toast import ToastNotifier

global notified, charged

toast = ToastNotifier()
bat = ps.sensors_battery()  # function returns bat.percent, bat.secsleft, bat.power_plugged


def print_bat_life():
    mm, ss = divmod(bat.secsleft, 60)
    hh, mm = divmod(mm, 60)
    print(f"Battery percentage: {bat.percent} Battery life: {hh}:{mm}")


def bat_check(enabled):
    if enabled:
        global notified
        global charged
        charged = False
        if charged is False:
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
        if (bat.power_plugged is False) and (bat.percent < 60):
            notified = False
            charged = False


def battery_check(enabled):
    global notified, charged
    bat = ps.sensors_battery()
    if enabled:
        if bat.percent < 60:
            notified = False
            charged = False

        elif bat.percent == 60 and bat.power_plugged:
            toast.show_toast(
                "Warning",
                "Battery has reached 60%",
                duration=20,
                icon_path="battery.ico",
                threaded=True,
            )
            notified = True
            charged = True

        if charged and notified and bat.percent < 60:
            notified = False
            charged = False
