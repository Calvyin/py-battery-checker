import batfunc as bf
import pystrayfunc as pf
import time
from pystray import Icon, MenuItem, Menu

starttime = time.monotonic()


menu = Menu(
    MenuItem("Enabled", pf.toggle),
    MenuItem("Quit", pf.on_quit)
)


icon = Icon("Battery Checker")
icon.menu = menu
icon.icon = pf.create_image(r"C:\Users\cyn_m\PycharmProjects\refactored-octo-system\src\battery.png")

while pf.is_toggled:
    bf.battery_check(pf.is_toggled)
    time.sleep(10.0 - ((time.monotonic() - starttime) % 10.0))



