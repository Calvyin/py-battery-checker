import psutil as ps
from win10toast import ToastNotifier
import os

global notified, charged
run = False
icon_path = os.path.abspath("battery.ico")

toast = ToastNotifier()
bat = ps.sensors_battery()  # function returns bat.percent, bat.secsleft, bat.power_plugged


def battery_check(enabled):
    global notified, charged, run
    bat = ps.sensors_battery()
    if enabled:
        if run is False:
            notified = False
            charged = False
            run = True

        if not notified and bat.percent >= 60 and bat.power_plugged:
            toast.show_toast(
                "Warning",
                "Battery has reached 60%",
                duration=10,
                icon_path=icon_path,
                threaded=True,
            )
            notified = True
            charged = True

        elif charged and notified and bat.percent < 60:
            notified = False
            charged = False
