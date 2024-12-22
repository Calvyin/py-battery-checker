from pystray import MenuItem, Menu
from PIL import Image
import sys

global is_toggled


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
    sys.exit()


def create_image(file_path):
    return Image.open(file_path)
