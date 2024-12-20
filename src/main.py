import functions as fs
import time

module_bat = True
starttime = time.monotonic()
while module_bat:
    fs.bat_check(module_bat)
    time.sleep(120.0 - ((time.monotonic() - starttime) % 120.0))
if module_bat is False:
    fs.bat_check(module_bat)



