import batfunc as bf
import pystrayfunc as pf
import time
from pystray import Icon, MenuItem, Menu

module_bat = True
starttime = time.monotonic()
while module_bat:
    bf.bat_check(module_bat)
    time.sleep(120.0 - ((time.monotonic() - starttime) % 120.0))
if module_bat is False:
    bf.bat_check(module_bat)


menu = Menu(
    MenuItem("Enabled", pf.toggle),
    MenuItem("Quit", pf.on_quit)
)


icon = Icon("Battery Checker")
icon.menu = menu
icon.icon = pf.create_image(r"C:\Users\cyn_m\PycharmProjects\refactored-octo-system\src\battery.png")