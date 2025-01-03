import psutil as ps
from win10toast import ToastNotifier

global notified, charged
run = False

toast = ToastNotifier()
bat = ps.sensors_battery()  # function returns bat.percent, bat.secsleft, bat.power_plugged


def print_bat_life():
    mm, ss = divmod(bat.secsleft, 60)
    hh, mm = divmod(mm, 60)
    print(f"Battery percentage: {bat.percent} Battery life: {hh}:{mm}")


def battery_check(enabled):
    global notified, charged, run
    bat = ps.sensors_battery()
    if enabled:
        if run is False:
            notified = False
            charged = False
            run = True

        if not notified and bat.percent >= 57 and bat.power_plugged:
            toast.show_toast(
                "Warning",
                "Battery has reached 60%",
                duration=20,
                icon_path="battery.ico",
                threaded=True,
            )
            notified = True
            charged = True

        elif charged and notified and bat.percent < 55:
            notified = False
            charged = False
