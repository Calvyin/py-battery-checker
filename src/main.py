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
icon.run_detached()

pf.notified = False
pf.charged = False
pf.run = False
pf.is_toggled = True

while pf.is_toggled:
    bf.battery_check(pf.is_toggled)
    time.sleep(12.0 - ((time.monotonic() - starttime) % 12.0))
