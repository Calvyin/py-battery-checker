import psutil as ps

bat = ps.sensors_battery()

print(bat.power_plugged)
print(bat.percent)