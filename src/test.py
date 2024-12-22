from pystray import Icon, MenuItem, Menu
from PIL import Image

is_toggled = True


def toggle(icon, item):
    global is_toggled
    is_toggled = not is_toggled
    icon.menu = Menu(
        MenuItem("Enabled" if is_toggled else "Disabled", toggle),
        MenuItem("Quit", on_quit)
    )
    print(is_toggled)
    icon.update_menu()


def on_quit(icon, item):
    icon.stop()


def create_image(file_path):
    return Image.open(file_path)


menu = Menu(
    MenuItem("Enabled", toggle),
    MenuItem("Quit", on_quit)
)

# Set up the icon
icon = Icon("Battery Checker")
icon.menu = menu
icon.icon = create_image(r"C:\Users\cyn_m\PycharmProjects\refactored-octo-system\src\battery.png")

# Run the icon
icon.run()
