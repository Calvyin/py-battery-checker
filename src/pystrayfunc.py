from pystray import MenuItem, Menu
import batfunc as bf
from PIL import Image
import os, time

starttime = time.monotonic()
is_toggled = True


def toggle(icon, item):
    global is_toggled
    is_toggled = not is_toggled
    icon.menu = Menu(
        MenuItem("Enabled" if is_toggled else "Disabled", toggle),
        MenuItem("Quit", on_quit)
    )
    icon.update_menu()


def on_quit(icon, item):
    icon.stop()
    os._exit(0)


def create_image(file_path):
    return Image.open(file_path)


def while_func():
    while is_toggled:
        bf.battery_check(is_toggled)
        time.sleep(12.0 - ((time.monotonic() - starttime) % 12.0))
